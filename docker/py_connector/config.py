# ThousandEyes Grafana Dashboard 1.0
# CISCO SAMPLE CODE LICENSE Version 1.1, Cisco Systems 2021, flopach

# ================================= #
#       ThousandEyes Settings       #
# ================================= #
base_url = "https://api.thousandeyes.com/v6" # define API base URL and API version
oauth_bearer_token = "" # Insert OAuth Bearer Token

# Test-Types to add to Dashboard
# page-load includes: (Web) Page load, (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# http-server includes: (Web) HTTP server, (Network) End-to-End metrics, (Network) Path visualization
# https://developer.thousandeyes.com/v6/test_data/
test_types = [ "page-load",
               "http-server"]

# set time window for historic data
# data will be retrieved from the specified amount of time ago up until the time of the request
# https://developer.thousandeyes.com/v6/#/timeranges
# examples: 12h --> 12 hours interval, 1d --> 24 hours interval
window = "1d"

# set time interval (in seconds) for pulling new data
interval = 60

# Enable specific dataset - Instead of getting all data per type, only request specific test IDs.
# You can request this data via code in main.py:
# all_tests = get_tests_by_type()
#    print(all_tests)
enable_specific_dataset = 0 #change to 1 to enable
specific_dataset = {
    'page-load': [{
        'testId': 0,
        'testName': "",
        'interval': 0
    }],
    'http-server': [{
        'testId': 0,
        'testName': "",
        'interval': 0
    }]
}



# ================================= #
#   DO NOT EDIT IF YOU ARE UNSURE   #
# ================================= #

# static config data for InfluxDBv2 
influx_token = "sensordata_token123"
influx_org = "sensordata_organization"
influx_bucket = "sensordata_bucket"
influx_url = "http://influxdb:8086" #docker http://influxdb:8086