# Flask Boilerplate

Boilerplate using Python's Flask web framework (https://flask.palletsprojects.com/en/2.2.x/) ready for bigger projects.

## Features

- Application factory pattern;
- Flask Blueprints for different application contexts;
- Poetry dependency manager;
- Pre-commit hooks:
    - end-of-file-fixer;
    - trailing-whitespace;
    - black;
    - autoflake;
    - flake8;
    - isort;
    - mypy.
- OpenAPI documentation (AKA Swagger);
- Testing with pytest;
- PostgreSQL Database connection with Flask-SQLAlchemy;
- Migrations with Flask-Migrate (Alembic);
- Docker and docker compose for deployment;
- HTTPS support with certbot (using Let's Encrypt);
- Nginx reverse proxy server;
- Bitbucket pipelines CICD.


## Install locally

Run `$ ./scripts/local-bootstrap.sh` to:

- Install poetry;
- Create virtual environment;
- Install dependencies;
- Set up git hook scripts.

Set up the Postgres database with the configuration as in docker-compose.yml (easiest way is to spin up a container for that service running `$ docker compose up database -d`)

Run `$ ./scripts/upgrade-db.sh` to run migrations.


## Activate environment

`$ source .venv/bin/activate`
## Run local server

`$ ./scripts/server.sh`

## Run tests

`$ poetry run pytest {pattern/options}`

Make sure there is a database named flask_app_test in the same db server as the local db

## Run lint

`$ poetry run pre-commit run --all-files`

## Swagger UI

at /docs


### Dockerfiles

`pipeline.Dockerfile` used to build base image to be used on the pipeline.

`nginx.Dockerfile` used to change nginx configuration.

`Dockerfile` to build the application.

### SSL configuration

Followed this tutorial: https://mindsers.blog/post/https-using-nginx-certbot-docker/

## License

Copyright © 2010-2022 [Imaginary Cloud](https://www.imaginarycloud.com/?utm_source=github). This library is licensed under the MIT license.

## About Imaginary Cloud

[![Imaginary Cloud](https://s3.eu-central-1.amazonaws.com/imaginary-images/Logo_IC_readme.svg)](https://www.imaginarycloud.com/?utm_source=github)

At Imaginary Cloud, we build world-class web & mobile apps. Our Front-end developers and UI/UX designers are ready to create or scale your digital product. Take a look at our [website](https://www.imaginarycloud.com/?utm_source=github) and [get in touch!](https://www.imaginarycloud.com/contacts/?utm_source=github) We'll take it from there.
