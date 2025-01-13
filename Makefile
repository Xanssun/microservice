DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml
REDIS_FILE = docker_compose/redis.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} ${ENV} up --build -d

.PHONY: redis
redis:
	${DC} -f ${REDIS_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: storage-down
storage-down:
	${DC} -f ${STORAGE_FILE} down

.PHONY: redis-down
redis-down:
	${DC} -f ${REDIS_FILE} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f


.PHONY: all
all:
	${DC} -f ${REDIS_FILE} -f ${STORAGE_FILE} -f ${APP_FILE} ${ENV} up --build -d
