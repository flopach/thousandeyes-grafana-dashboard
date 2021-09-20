FROM python:3.9-slim

RUN pip install influxdb_client requests 

COPY config.py /py_connector/
COPY main.py /py_connector/
COPY influxdb_connect.py /py_connector/

CMD ["python", "-u", "/py_connector/main.py"]