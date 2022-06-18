### FAST API - Endpoints 

This repository contains API endpoints built for a 
blog application.

Technologies used:
- Fast API
- Sqlachemy
- Alembic
- Postgres
- Uvicorn 
- Docker

### Running

```pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 "uvicorn[standard]" python-dotenv```

```docker-compose build ```

```docker-compose up```

docker-compose run app alembic revision --autogenerate -m "New Migration" 
docker-compose run app 
alembic upgrade head