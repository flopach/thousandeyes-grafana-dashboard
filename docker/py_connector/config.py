# ThousandEyes Grafana Dashboard 1.0.1
# CISCO SAMPLE CODE LICENSE Version 1.1, Cisco Systems 2021, flopach

# IMPORTANT: If you already did once "docker-compose up" and want to change the settings,
# you have to rebuild the Docker Container: "docker-compose build"

# ================================= #
#       ThousandEyes Settings       #
# ================================= #

base_url = "https://api.thousandeyes.com/v6" # define API base URL and API version
#oauth_bearer_token = "62d3ea54-b962-468c-b742-f78f59b8e1ef" # Insert OAuth Bearer Token
oauth_bearer_token = "xxxxxxxx"

### 2 Options: py_connector will ADD tests based on this input from your ThousandEyes dashboard:
# 0 = add ALL test types as stated in test_types 
# 1 = add ALL test types as stated in test_types AND which are TAGGED with the stated label_name
# Create your test label at https://app.thousandeyes.com/settings/tests/?tab=labels
enable_label_specific = 1 #change to 1 or 0
label_name = "mylabel" #case sensitive!


### Define test types which should be added
# py_connector will add ALL test types below. You can specify the test type by removing one.
# page-load includes: (Web) Page load, (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# http-server includes: (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# More information: https://developer.thousandeyes.com/v6/test_data/
test_types = [ "page-load",
               "agent-to-agent",
               "agent-to-server",
               "http-server"]


### Set time window for historic data
# data will be retrieved from the specified amount of time ago up until the time of the request
# https://developer.thousandeyes.com/v6/#/timeranges
# examples: 12h --> 12 hours interval, 1d --> 24 hours interval
window = "1d"


### Set time interval (in seconds) for pulling new data
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
