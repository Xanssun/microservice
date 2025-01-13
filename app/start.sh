#!/bin/bash

# Ожидание подключения к PostgreSQL
python3 /app/core/wait_for_postgres.py

# Выполнение миграций Alembic
alembic -c /app/alembic.ini revision --autogenerate -m 'add migrations'
alembic -c /app/alembic.ini upgrade head

# Запуск приложения
uvicorn --factory application.api.main:create_app --reload --host 0.0.0.0 --port 8000
