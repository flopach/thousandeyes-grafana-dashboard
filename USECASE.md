ThousandEyes Grafana Dashboard
=====================================

Extract data from the **ThousandEyes REST API** and visualize it on your customized Grafana Dashboard. Deploy Grafana, InfluxDBv2 and the Python connector script within a few minutes.

![](images/te-grafana.png)

**Supported Functions**

* Get **historic data** (custom time range) and **pull new data** (set your own interval) from your ThousandEyes tests.
* Grafana, a sample Dashboard-template and InfluxDBv2 are already pre-configured
* Collected data is persistent! It will remain untouched even after the containers will be restarted.
* Currently Supported Tests:
	* (Web) Page load
	* (Web) HTTP server
	* (Network) End-to-End metrics
	* (Network) Path visualization

## Visuals

**Prepare:** Create Label (optional), clone git-repo, change settings in config.py

![](images/te-grafana-dashboard_prepare.gif)

**Run:** Start containers, copy and insert testId into Grafana

![](images/te-grafana-dashboard_run.gif)

