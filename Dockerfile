ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

EXPOSE 2000

CMD ["gunicorn", "--bind", "0.0.0.0:2020", "wsgi:app"]