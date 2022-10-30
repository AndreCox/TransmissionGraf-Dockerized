#!/usr/bin/python3
import os
homedir = './'
TransmissionGrafFolder=str(homedir + "/Scripts/TransmissionGraf/")
GeoIPDBfile=str(TransmissionGrafFolder + "GeoLite2-City.mmdb")
TransmissionGrafFileinfo=str(TransmissionGrafFolder + ".fileinfo")
TransmissionGrafPeerinfo=str(TransmissionGrafFolder + ".peerinfo")
TransmissionGrafSummary=str(TransmissionGrafFolder + ".transmissionsummary")

TransmissionHost=os.getenv('TRANSMISSION_HOST', '192.168.0.1')
TransmissionPort=os.getenv('TRANSMISSION_PORT', '9091')
TransmissionUsername=os.getenv('TRANSMISSION_USERNAME', 'transmission')
TransmissionPassword=os.getenv('TRANSMISSION_PASSWORD', 'transmission')

InfluxDBHost=os.getenv('INFLUXDB_HOST', '192.168.0.1')
InfluxDBPort=os.getenv('INFLUXDB_PORT', '8086')
InfluxDBUsername=os.getenv('INFLUXDB_USERNAME', 'influxdb')
InfluxDBPassword=os.getenv('INFLUXDB_PASSWORD', 'influxdb')
InfluxDBDatabase=os.getenv('INFLUXDB_DATABASE', 'default')
