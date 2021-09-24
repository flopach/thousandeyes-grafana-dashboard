# ThousandEyes Grafana Dashboard 1.0
# CISCO SAMPLE CODE LICENSE Version 1.1, Cisco Systems 2021, flopach

# ================================= #
#       ThousandEyes Settings       #
# ================================= #
base_url = "https://api.thousandeyes.com/v6" # define API base URL and API version
oauth_bearer_token = "" # Insert OAuth Bearer Token

##  Default: py_connector will add ALL test types below
# page-load includes: (Web) Page load, (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# http-server includes: (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# https://developer.thousandeyes.com/v6/test_data/
test_types = [ "page-load",
               "http-server"]

## Option: Enable label specific tests
# py_connector will add test types which are TAGGED with the stated label_name
# Create your test label at https://app.thousandeyes.com/settings/tests/?tab=labels
enable_label_specific = 1 #change to 1 to enable
label_name = "grafana"

## Set time window for historic data
# data will be retrieved from the specified amount of time ago up until the time of the request
# https://developer.thousandeyes.com/v6/#/timeranges
# examples: 12h --> 12 hours interval, 1d --> 24 hours interval
window = "1d"

## Set time interval (in seconds) for pulling new data
interval = 60

# IMPORTANT: If you already did once "docker-compose up" and want to change the settings,
# you have to rebuild the Docker Container: "docker-compose build"



# ================================= #
#   DO NOT EDIT IF YOU ARE UNSURE   #
# ================================= #

# static config data for InfluxDBv2 
influx_token = "sensordata_token123"
influx_org = "sensordata_organization"
influx_bucket = "sensordata_bucket"
influx_url = "http://influxdb:8086" #docker http://influxdb:8086