# ThousandEyes Grafana Dashboard

Extract data from the ThousandEyes REST API and visualize it on your customized Grafana Dashboard. Deploy Grafana, InfluxDBv2 and the Python connector script within a few minutes.

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

**Dashboard-Template Screenshots**

![](images/grafana-dashboard1.png)

![](images/grafana-dashboard2.png)

## Installation

### Prerequisites

* git, Docker/Docker-compose installed

### Installation Steps

1. Clone repository

```
git clone https://github.com/flopach/thousandeyes-grafana-dashboard.git
```

2. Change your desired settings in the **docker/py_connector/config.py** file.

3. Start all containers _from_ the docker/ directory. This may take some minutes.

```
docker-compose up
```

More useful commands:

* Run as daemon mode: `docker-compose up -d`
* Stops containers: `docker-compose down`
* Build again the containers (when you changed the Python scripts): `docker-compose build`

## Configuration

### Configure: config.py
Simply open `docker/py_connector/config.py` in any text-editor to set your desired configuration.

* Create OAuth Bearer Token: **Account Settings** > **Users and Roles** >> **User API Tokens**
* 2 data selection options:
	* Default: py_connector will add ALL HTTP-Server  and Page-Load tests
	* Option: py_connector will add ONLY tests with the defined label
* time window
* pull interval

Example: When you've created a ThousandEyes page-load test (see below), you will receive data from 4 views:

![](images/te-test-ui.png)

### Configure: Dashboards

Login to Grafana dashboard and configure your dashboard modules by inserting the ThousandEyes testId. Additionally, use the query editor from the InfluxDB UI as a help to create and copy the Flux language syntax snippet.

Login **Grafana** - [http://localhost:3000](http://localhost:3000)

* username: admin
* password: admin123

Login **InfluxDB** - [http://localhost:8086](http://localhost:3000)

* username: admin
* password: admin123

### Configure: docker-compose.yml (optional)
If you are not familiar with Docker compose, go ahead to check the [documentation](https://docs.docker.com/compose/). Basically, 4 containers will be spun up:

* InfluxDBv2: data will be stored outside of the container
* InfluxDBv2 CLI setup instance: Will setup the other InfluxDBv2 container if it is not setup yet
* Grafana Dashboard: configuration settings will be stored outside of the container
* Py connector: Python connector scripts (stored in the `py_connector` folder)

## Good to knows

**- InfluxDB Setup Error**

When you have already started docker-compose and are re-starting the containers, this error is normal:

```
influxdb_setup_1  | Error: instance at "http://influxdb:8086" has already been setup
influxdb_setup_1  | See 'influx setup -h' for help
influxdb_setup_1 exited with code 1
```

**- Changing the settings in config.py**

When you have already started docker-compose once and would like to change the settings, you need to re-build the py_connector container:

```
docker-compose build
```

## Versioning

**1.0** (Sep 2021) - Initial version

**1.0.1** (Dec 2021) - Bugfix: You can now add only one test type which is tagged. config.py Update.

## License

This project is licensed under the Cisco Samplel Code License 1.1 - see the [LICENSE.md](LICENSE.md) file for details

## Further Links

* [Cisco DevNet Website](https://developer.cisco.com)