FROM python:3.8-slim-buster

ARG POETRY_VERSION
ARG PROD_MODE

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
        && poetry install $(test "$PROD_MODE" == true && echo "--no-dev") --no-interaction --no-ansi

EXPOSE 8002

COPY . /code

RUN poetry shell

ENTRYPOINT ["python", "app/manage.py", "runserver", "0.0.0.0:8002"]
