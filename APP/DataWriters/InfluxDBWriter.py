import os
from influxdb_client import InfluxDBClient, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.exceptions import InfluxDBError
from ErrorHandling.ConsoleLogger import ConsoleLogger  # Přidejte toto

class InfluxDBWriter:
    def __init__(self):
        self.console_logger = ConsoleLogger()  # Přidejte toto
        self.console_logger.log_info("Initializing InfluxDBWriter...")

        influx_url = os.getenv('INFLUX_URL')
        influx_token = os.getenv('INFLUX_TOKEN')
        influx_org = os.getenv('INFLUX_ORG')

        if None in (influx_url, influx_token, influx_org):
            self.console_logger.log_error("One or more required environment variables for InfluxDBWriter are missing.")
            raise ValueError("One or more required environment variables for InfluxDBWriter are missing.")

        self.client = InfluxDBClient(
            url=influx_url,
            token=influx_token,
            org=influx_org
        )

    def write_to_influx(self, point, bucket):
        self.console_logger.log_info("Writing data to InfluxDB...")
        with self.client.write_api(write_options=SYNCHRONOUS) as writer:
            try:
                writer.write(bucket=bucket, record=[point])
                self.console_logger.log_info("Data written to InfluxDB successfully.")
            except InfluxDBError as e:
                self.console_logger.log_error(f"Error writing data to InfluxDB: {e}")
                self.console_logger.log_error(f"Printing to stderr: {e}")
