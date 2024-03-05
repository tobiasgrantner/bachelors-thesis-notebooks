compose type *actions:
    @docker compose -f compose/{{type}}/docker-compose.yml {{actions}}

userdb *actions:
    @docker ps -a -q --filter name=dbrepo-userdb-* | xargs -r docker {{actions}}

start type: (userdb "start") (compose type "up" "-d")

stop type: (userdb "stop") (userdb "rm") (compose type "down")

remove type: (userdb "stop") (userdb "rm" "-v") (compose type "down" "-v")