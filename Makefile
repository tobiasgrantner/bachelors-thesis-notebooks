start-before:
	docker compose -f compose/before/docker-compose.yml up -d
	docker ps -a -q --filter "name=dbrepo-userdb-*" | xargs -r docker start

start-after:
	docker compose -f compose/after/docker-compose.yml up -d

start-queue:
	docker compose -f compose/queue/docker-compose.yml up -d

stop-before:
	docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker stop
	docker compose -f compose/before/docker-compose.yml down

stop-after:
	docker compose -f compose/after/docker-compose.yml down

stop-queue:
	docker compose -f compose/queue/docker-compose.yml down

remove-before:
	docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker stop
	docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker rm -v
	docker compose -f compose/before/docker-compose.yml down -v
	docker volume ls -q --filter name=dbrepo-userdb-* | xargs -r docker volume rm

remove-after:
	docker compose -f compose/after/docker-compose.yml down -v

remove-queue:
	docker compose -f compose/queue/docker-compose.yml down -v