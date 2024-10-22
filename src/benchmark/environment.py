from typing import Literal, get_args
from benchmark.process import run


State = Literal["before", "after"]
Improvement = Literal["environment-independence", "service-merge"]

STATES = list(get_args(State))
IMPROVEMENTS = list(get_args(Improvement))


def start(improvement: Improvement, state: State) -> None:
    run(f"docker compose -f compose/{improvement}/{state}/docker-compose.yml up -d")

    if state == "before" and improvement == "environment-independence":
        run('docker ps -a -q --filter "name=dbrepo-userdb-*" | xargs -r docker start')


def stop(improvement: Improvement, state: State) -> None:
    if state == "before" and improvement == "environment-independence":
        run("docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker stop")

    run(f"docker compose -f compose/{improvement}/{state}/docker-compose.yml down")

    if state == "before" and improvement == "environment-independence":
        run(
            "docker volume ls -q --filter name=dbrepo-userdb-* | xargs -r docker volume rm"
        )


def remove(improvement: Improvement, state: State) -> None:
    if state == "before" and improvement == "environment-independence":
        run("docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker stop")
        run("docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker rm -v")

    run(f"docker compose -f compose/{improvement}/{state}/docker-compose.yml down -v")
