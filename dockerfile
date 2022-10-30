FROM python:3.8-slim-buster
RUN pip3 install influxdb

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y transmission-cli
RUN mkdir -p Scripts/TransmissionGraf

COPY src .
CMD ["python3", "TG.py"]