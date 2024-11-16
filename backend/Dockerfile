FROM python:3.12-alpine

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./alembic.ini /app/alembic.ini
COPY ./src /app/src
COPY ./entry.sh /app/entry.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV IS_PROD 1

ENTRYPOINT [ "sh", "entry.sh" ]