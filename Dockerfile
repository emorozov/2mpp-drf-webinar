FROM python:3.12.0-alpine3.18 AS django-static-builder

RUN pip install --no-cache-dir poetry==1.7.1

COPY . /app/src

WORKDIR /app/src

RUN poetry config virtualenvs.in-project true && \
    poetry install --no-interaction --no-ansi

RUN /app/src/.venv/bin/python profiles/manage.py collectstatic --no-input


FROM python:3.12.0-alpine3.18 AS django-api

COPY --from=django-static-builder /app/src /app/src/

WORKDIR /app/src

CMD /app/src/.venv/bin/python profiles/manage.py runserver 0.0.0.0:8000


FROM nginx:1.25.3-alpine AS front

COPY --from=django-static-builder /app/src/static /data/static

