FROM python:3.8-slim-buster

ARG POETRY_VERSION

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
        && poetry install --no-dev --no-interaction --no-ansi

EXPOSE 8002

COPY . /code

RUN poetry shell

WORKDIR /code/app

ENTRYPOINT []
