# ThousandEyes Grafana Dashboard 1.0
# CISCO SAMPLE CODE LICENSE Version 1.1, Cisco Systems 2021, flopach

from influxdb_client import InfluxDBClient, WritePrecision, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import config
from urllib3 import Retry

#influxdb connect
retries = Retry(connect=10, read=5, redirect=10)
influx_client = InfluxDBClient(url=config.influx_url, token=config.influx_token, org=config.influx_org,retries=retries) #debug=True
write_api = influx_client.write_api(write_options=SYNCHRONOUS)