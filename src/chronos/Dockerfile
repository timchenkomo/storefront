FROM python:3

RUN apt-get update && apt-get install cron rsyslog -y && \
    pip install sqlalchemy psycopg2-binary
WORKDIR /app
COPY crontab /var/spool/cron/crontabs/root
COPY . .
RUN chmod a+x /app/scan_products.py && \
    chmod a+x /app/entrypoint.sh
CMD [ "/app/entrypoint.sh" ]
