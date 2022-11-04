###############################################
# Base Image
###############################################
FROM python:3.9.4-slim-buster as python-base

ENV PYTHONUNBUFFERED=1  \
    PYTHONDONTWRITEBYTECODE=1  \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


##############################################
# Builder Image
##############################################
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

# ###############################################
# # Production Image
# ###############################################
# FROM python-base as production
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY ./app ./app
COPY ./migrations ./migrations
COPY ./config ./config

# CMD [ "poetry", "run" , "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "\'app:create_app(env=\"prod\")\'"]
CMD poetry run gunicorn -w 4 --bind 0.0.0.0:5000 'app:create_app(env="prod")'
