FROM python:3 as build
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install

FROM build
COPY . .
CMD [ "sh", "-c", "./entrypoint.sh" ]
