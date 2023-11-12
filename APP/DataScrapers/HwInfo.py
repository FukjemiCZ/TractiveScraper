import asyncio
from aiotractive import Tractive
from DataConvertors.Influx.HwInfo import HwInfo
from DataWriters.InfluxDBWriter import InfluxDBWriter
import datetime

class TractiveHwInfo:
    def __init__(self, config):
        self.tracker_id = config['tracker_id']
        self.influx_bucket = config['influx_bucket']
        self.tractive_mail = config['tractive_mail']
        self.tractive_pass = config['tractive_pass']

    async def process_data(self):
        data = await self.get_data_from_tractive()
        self.write_data_to_influx(data)

    async def get_data_from_tractive(self):
        async with Tractive((self.tractive_mail), self.tractive_pass) as client:
            tracker = client.tracker(self.tracker_id)
            return await tracker.hw_info()

    def write_data_to_influx(self, data):
        influx_writer = InfluxDBWriter()
        hwinfo_entry = HwInfo(data).get_point()
        influx_writer.write_to_influx(hwinfo_entry, self.influx_bucket)
