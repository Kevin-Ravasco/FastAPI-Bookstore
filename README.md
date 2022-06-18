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
Install the required dependencies:

```pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 "uvicorn[standard]" python-dotenv```

Docker commands:

```docker-compose build ```

```docker-compose up```

After installing alembic, we can initialize it in a 
directory called alembic by running:

```alembic init alembic```

To run migrations in the docker container, run:
```docker-compose run app alembic revision --autogenerate -m "New Migration" ```

docker-compose run app 

alembic upgrade head