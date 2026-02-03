FROM postgres:18.1

RUN apt-get update -y && \
    apt-get install -y \
      postgresql-server-dev-18 \
      postgresql-plpython3-18 \
      postgis \
      postgresql-18-postgis-3 \
      postgresql-18-cron \
      lsb-release \
      wget \
      gnupg2 \
      ca-certificates

RUN echo "deb https://packagecloud.io/timescale/timescaledb/debian/ $(lsb_release -c -s) main" | tee /etc/apt/sources.list.d/timescaledb.list
RUN wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | gpg --dearmor -o /etc/apt/trusted.gpg.d/timescaledb.gpg
RUN apt-get update -y && \
    apt-get install -y timescaledb-2-postgresql-18

RUN echo "shared_preload_libraries = 'pg_cron,timescaledb'" >> /usr/share/postgresql/postgresql.conf.sample
RUN echo "cron.database_name = 'layrz'" >> /usr/share/postgresql/postgresql.conf.sample
RUN echo "wal_level = 'logical'" >> /usr/share/postgresql/postgresql.conf.sample
RUN echo "max_wal_senders = 10" >> /usr/share/postgresql/postgresql.conf.sample
RUN echo "max_replication_slots = 10" >> /usr/share/postgresql/postgresql.conf.sample

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER postgres

RUN pip3 install -U layrz-sdk paho-mqtt --user --break-system-packages

USER root

EXPOSE 5432
