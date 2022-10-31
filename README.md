# TransmissionGraf Dockerized
Is a program which provides transmission-daemon info to InfluxDB  

The original script was made by [@Festeazy](https://github.com/Festeazy/TransmissionGraf) I have taken the script and updated it to run in a Docker Container as well as fixing a couple minor bugs that would cause a program crash.   

## Installation
You can run this program from the command line or via docker compose.
This uses influxdb 1.0 auth so you will need to set that up if using influxdb 2.0 this [link](https://docs.influxdata.com/influxdb/cloud/reference/cli/influx/v1/auth/create/) may help you create a v1.0 compatible api endpoint.
```yml
---
version: '2'
services:
  transmission-graf:
    image: andrerc1/transmission-graf:latest
    container_name: transmission-graf
# if you are running this next to influx db you can add this to make sure that this service only starts when influx has already started.
#   depends_on:
#     - influxdb
    environment:
      # transmission host config
      TRANSMISSION_USERNAME: transmission
      TRANSMISSION_PASSWORD: transmission
      TRANSMISSION_PORT: 9001
      TRANSMISSION_HOST: 192.168.0.1
      # InfluxDB config
      INFLUXDB_USERNAME: influxdb
      INFLUXDB_PASSWORD: influxdb
      INFLUXDB_HOST: 192.168.0.1
      INFLUXDB_PORT: 8086
      INFLUXDB_DATABASE: default
    restart: always
```

![image](https://user-images.githubusercontent.com/65983438/82976070-c4e44000-9fa3-11ea-862a-5003606e5fc5.png)
![TransGraf](https://user-images.githubusercontent.com/65983438/83154918-4c29d480-a0c6-11ea-9278-03c4e04c6c86.png)


- Released May 29th 2020! 
- Updated October 30th 2022! 

