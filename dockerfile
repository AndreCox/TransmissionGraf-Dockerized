FROM python:3.8-slim-buster

RUN pip3 install influxdb

WORKDIR /app

ENV TRANSMISSION_HOST=192.168.0.1
ENV TRANSMISSION_PORT=9091
ENV TRANSMISSION_USERNAME=transmission
ENV TRANSMISSION_PASSWORD=transmission

ENV INFLUXDB_HOST=192.168.0.1
ENV INFLUXDB_PORT=8086
ENV INFLUXDB_USERNAME=influxdb
ENV INFLUXDB_PASSWORD=influxdb
ENV INFLUXDB_DATABASE=default

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y transmission-cli
RUN mkdir -p Scripts/TransmissionGraf

COPY src .
COPY GeoLite2-City.mmdb Scripts/TransmissionGraf

CMD ["python", "main.py"]