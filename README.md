# Решение задания "Backend" по практике ITLABS
### На папку frontend не смотрите, хотел ещё сделать второе задание, но по обстоятельствам не успел

### Запуск проекта через Docker
Для запуска переименуйте .env.example в .env (настраивать не надо, environment прописаны в docker-compose.yaml)<br>
В корне проекта прописать
```shell
    docker compose up --build -d
```
Команда соберёт 2 контейнера:
1. База данных (PostgreSQL) 
2. App (миграции alembic + backend fastapi)


### Запуск проекта через cmd
Для запуска переименуйте .env.example в .env и настроить переменные для подключения к БД PostgreSQL<br>
В корне проекта прописать
```shell
    pip install uv
    uv venv
    .venv\Scripts\activate
    uv sync --no-dev
    alembic upgrade head
    python -m src.main
```

### Ссылки проекта
* Admin panel - http://localhost:8081/admin
* Swagger - http://localhost:8081/ui-swagger

### Используемый стек технологий
* Python 3.12 - язык программирования на котором разрабатывался проект
* PostgreSQL - используемая БД в проекте
* SQLAlchemy 2.0.41 - ORM система для работы с БД
* AsyncPg 0.30.0 - асинхронный коннектор для связи с БД
* Alembic 1.16.2 - миграции БД
* SQLAdmin 0.20.1 - админ панель
* FastAPI 0.115.13 - фреймворк на котором разрабатывался проект
