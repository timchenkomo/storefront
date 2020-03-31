FROM python:3 as build
RUN apt-get update && apt-get install cron rsyslog -y
RUN pip install sqlalchemy psycopg2-binary

FROM build
COPY crontab /etc/crontab
WORKDIR /app
COPY . .
RUN chmod a+x /app/scan_products.py && \
    chmod a+x /app/entrypoint.sh
CMD [ "/app/entrypoint.sh" ]
