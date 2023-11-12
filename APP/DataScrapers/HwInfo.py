import asyncio
from ErrorHandling.ConsoleLogger import ConsoleLogger  # Přidejte toto
from aiotractive import Tractive
from DataConvertors.Influx.HwInfo import HwInfo
from DataWriters.InfluxDBWriter import InfluxDBWriter
import datetime
import logging

# Configure custom logging
console_logger = ConsoleLogger()

# Configure logging
console_logger.log_info("Configuring logging...")  # Přidejte toto
logging.basicConfig(filename='tractive_hwinfo_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TractiveHwInfo:
    def __init__(self, config):
        self.console_logger = ConsoleLogger()  # Přidejte toto
        self.console_logger.log_info("Initializing TractiveHwInfo...")  # Přidejte toto

        self.tracker_id = config['tracker_id']
        self.influx_bucket = config['influx_bucket']
        self.tractive_mail = config['tractive_mail']
        self.tractive_pass = config['tractive_pass']

    async def process_data(self):
        self.console_logger.log_info("Processing HwInfo data...")
        try:
            data = await self.get_data_from_tractive()
            self.write_data_to_influx(data)
            self.console_logger.log_info("HwInfo data processing completed.")
        except Exception as e:
            self.console_logger.log_error(f"Error processing HwInfo data: {e}")

    async def get_data_from_tractive(self):
        self.console_logger.log_info("Fetching HwInfo data from Tractive...")
        try:
            async with Tractive((self.tractive_mail), self.tractive_pass) as client:
                tracker = client.tracker(self.tracker_id)
                return await tracker.hw_info()
        except Exception as e:
            self.console_logger.log_error(f"Error fetching HwInfo data from Tractive: {e}")
            return {}

    def write_data_to_influx(self, data):
        self.console_logger.log_info("Writing HwInfo data to InfluxDB...")
        try:
            influx_writer = InfluxDBWriter()
            hwinfo_entry = HwInfo(data).get_point()
            influx_writer.write_to_influx(hwinfo_entry, self.influx_bucket)
            self.console_logger.log_info("HwInfo data written to InfluxDB successfully.")
        except Exception as e:
            self.console_logger.log_error(f"Error writing HwInfo data to InfluxDB: {e}")
