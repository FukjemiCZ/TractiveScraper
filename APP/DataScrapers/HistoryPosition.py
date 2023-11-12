import asyncio
from ErrorHandling.ConsoleLogger import ConsoleLogger  # Přidejte toto
from aiotractive import Tractive
from DataConvertors.Influx.LocationHistory import LocationHistory
from DataWriters.InfluxDBWriter import InfluxDBWriter
import datetime
import logging

# Configure custom logging
console_logger = ConsoleLogger()

# Configure logging
console_logger.log_info("Configuring logging...")  # Přidejte toto
logging.basicConfig(filename='tractive_history_position_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TractiveHistoryPosition:
    def __init__(self, config):
        self.console_logger = ConsoleLogger()  # Přidejte toto
        self.console_logger.log_info("Initializing TractiveHistoryPosition...")  # Přidejte toto

        self.tracker_id = config['tracker_id']
        self.influx_bucket = config['influx_bucket']
        self.tractive_mail = config['tractive_mail']
        self.tractive_pass = config['tractive_pass']
        self.last_sec = config['last_sec']

    async def process_data(self):
        self.console_logger.log_info("Processing LocationHistory data...")
        try:
            now = datetime.datetime.now().timestamp()
            time_from = now - int(self.last_sec)
            time_to = now
            data = await self.get_data_from_tractive(time_from, time_to)
            self.write_data_to_influx(data)
            self.console_logger.log_info("LocationHistory data processing completed.")
        except Exception as e:
            self.console_logger.log_error(f"Error processing LocationHistory data: {e}")

    async def get_data_from_tractive(self, time_from, time_to):
        self.console_logger.log_info("Fetching LocationHistory data from Tractive...")
        try:
            async with Tractive((self.tractive_mail), self.tractive_pass) as client:
                tracker = client.tracker(self.tracker_id)
                return await tracker.positions(time_from, time_to, "json_segments")
        except Exception as e:
            self.console_logger.log_error(f"Error fetching LocationHistory data from Tractive: {e}")
            return []

    def write_data_to_influx(self, data):
        self.console_logger.log_info("Writing LocationHistory data to InfluxDB...")
        try:
            influx_writer = InfluxDBWriter()
            for entry in data[0]:
                location_entry = LocationHistory(entry, self.tracker_id).get_point()
                influx_writer.write_to_influx(location_entry, self.influx_bucket)
            self.console_logger.log_info("LocationHistory data written to InfluxDB successfully.")
        except Exception as e:
            self.console_logger.log_error(f"Error writing LocationHistory data to InfluxDB: {e}")
