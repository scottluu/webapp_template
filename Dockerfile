FROM node:current-bullseye-slim as node-builder

WORKDIR /caffiends/frontend

COPY frontend .

WORKDIR /caffiends/frontend

RUN yarn && yarn build


FROM python:3.10.7-slim-bullseye

WORKDIR /caffiends

RUN python -m venv venv && ./venv/bin/pip install poetry
COPY app.py .
COPY poetry.lock .
COPY pyproject.toml .
RUN ./venv/bin/poetry install

WORKDIR /caffiends/frontend/build

COPY --from=node-builder /caffiends/frontend/build .

CMD ./venv/bin/uvicorn app:app --port 8080
