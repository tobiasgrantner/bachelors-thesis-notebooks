from abc import abstractmethod
from os import PathLike
from typing import Any, Iterable, Mapping
from requests import get, post, delete, put
from time import time_ns
from tusclient.client import TusClient


class Api:

    def __init__(
        self,
        client_id: str = "dbrepo-client",
        client_secret: str = "MUwRc7yfXSJwX8AdRMWaQC3Nep1VjwgG",
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username: str
        self.password: str
        self.token: str
        self.validity: int = -1

    def _get_token(self):
        if time_ns() + 1e9 < self.validity:
            return self.token

        response = post(
            "http://localhost/api/auth/realms/dbrepo/protocol/openid-connect/token",
            data={
                "username": self.username,
                "password": self.password,
                "grant_type": "password",
                "client_id": self.client_id,
                "scope": "openid",
                "client_secret": self.client_secret,
            },
        )
        response.raise_for_status()
        json = response.json()
        self.token = json["access_token"]
        self.validity = time_ns() + json["expires_in"] * 1e9
        return self.token

    def _get_headers(self):
        if self.validity < 0:
            return {}

        return {"Authorization": f"Bearer {self._get_token()}"}

    @abstractmethod
    def _database_url(self, database_id: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def create_database(self, name: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def _upload_file(self, file: str | PathLike) -> str:
        raise NotImplementedError

    def create_user(self, username: str, password: str, email: str) -> int:
        response = post(
            "http://localhost/api/user",
            json={
                "username": username,
                "password": password,
                "email": email,
            },
        )
        response.raise_for_status()
        return response.json()["id"]

    def login(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self._get_token()

    def create_table(
        self,
        database_id: int,
        name: str,
        description: str = "",
        columns: Iterable[Mapping[str, Any]] = [],
        constraints: Mapping[str, Any] | None = None,
    ) -> int:
        response = post(
            f"{self._database_url(database_id)}/table",
            headers=self._get_headers(),
            json={
                "name": name,
                "description": description if description else name,
                "columns": columns,
                "constraints": constraints,
            },
        )
        response.raise_for_status()
        return response.json()["id"]

    def insert_row(
        self, database_id: int, table_id: int, data: Mapping[str, Any]
    ) -> None:
        response = post(
            f"{self._database_url(database_id)}/table/{table_id}/data",
            headers=self._get_headers(),
            json={
                "data": data,
            },
        )
        response.raise_for_status()

    def update_row(
        self,
        database_id: int,
        table_id: int,
        keys: Mapping[str, Any],
        data: Mapping[str, Any],
    ) -> None:
        response = put(
            f"{self._database_url(database_id)}/table/{table_id}/data",
            headers=self._get_headers(),
            json={
                "keys": keys,
                "data": data,
            },
        )
        response.raise_for_status()

    def delete_row(
        self, database_id: int, table_id: int, keys: Mapping[str, Any]
    ) -> None:
        response = delete(
            f"{self._database_url(database_id)}/table/{table_id}/data",
            headers=self._get_headers(),
            json={
                "keys": keys,
            },
        )
        response.raise_for_status()

    def import_csv(self, database_id: int, table_id: int, file: str | PathLike) -> None:
        server_file = self._upload_file(file)

        response = post(
            f"{self._database_url(database_id)}/table/{table_id}/data/import",
            headers=self._get_headers(),
            json={
                "separator": ",",
                "skip_lines": 1,
                "location": server_file,
            },
        )
        response.raise_for_status()

    def create_query(self, database_id: int, query: str) -> Mapping[str, Any]:
        response = post(
            f"{self._database_url(database_id)}/query",
            headers=self._get_headers(),
            json={
                "statement": query,
                "timestamp": None,
            },
        )
        response.raise_for_status()
        return response.json()

    def execute_query(self, database_id: int, query_id: int) -> Mapping[str, Any]:
        response = get(
            f"{self._database_url(database_id)}/query/{query_id}/data",
            headers=self._get_headers(),
        )
        response.raise_for_status()
        return response.json()


class ApiBefore(Api):

    def _database_url(self, database_id: int) -> str:
        return f"http://localhost/api/container/{database_id}/database/{database_id}"

    def create_database(self, name: str) -> int:
        response = post(
            "http://localhost/api/container",
            headers=self._get_headers(),
            json={
                "name": name,
                "repository": "mariadb",
                "tag": "10.5",
            },
        )
        response.raise_for_status()
        container_id = response.json()["id"]

        response = put(
            f"http://localhost/api/container/{container_id}",
            headers=self._get_headers(),
            json={
                "action": "start",
            },
        )
        response.raise_for_status()

        response = post(
            f"http://localhost/api/container/{container_id}/database",
            headers=self._get_headers(),
            json={
                "name": name,
                "is_public": True,
            },
        )
        response.raise_for_status()

        if not container_id == response.json()["id"]:
            raise ValueError("Database and container IDs do not match")

        return container_id

    def _upload_file(self, file: str | PathLike) -> str:
        with open(file, "rb") as f:
            response = post(
                "http://localhost/server-middleware/upload",
                headers=self._get_headers(),
                files={
                    "file": f,
                },
            )
        response.raise_for_status()
        return response.json()["path"]


class ApiAfter(Api):

    def _database_url(self, database_id: int) -> str:
        return f"http://localhost/api/database/{database_id}"

    def create_database(self, name: str) -> int:
        response = post(
            "http://localhost/api/database",
            headers=self._get_headers(),
            json={
                "name": name,
                "container_id": 1,
                "is_public": True,
            },
        )
        response.raise_for_status()
        return response.json()["id"]

    def _upload_file(self, file: str | PathLike) -> str:
        client = TusClient(
            "http://localhost/api/upload/files", headers=self._get_headers()
        )
        uploader = client.uploader(str(file))
        uploader.upload()

        return f'/tmp/{uploader.url.split("/")[-1]}'
