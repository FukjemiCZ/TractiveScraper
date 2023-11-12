import sys
import os
from influxdb_client import InfluxDBClient, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.exceptions import InfluxDBError

class InfluxDBWriter:
    def __init__(self):
        self.client = InfluxDBClient(
            url=os.getenv('INFLUX_URL'),
            token=os.getenv('INFLUX_TOKEN'),
            org=os.getenv('INFLUX_ORG')
        )

    def write_to_influx(self, point, bucket):
        with self.client.write_api(write_options=SYNCHRONOUS) as writer:
            try:
                writer.write(bucket=bucket, record=[point])
            except InfluxDBError as e:
                self.print_to_stderr(e)

    @staticmethod
    def print_to_stderr(message):
        print(message, file=sys.stderr)
