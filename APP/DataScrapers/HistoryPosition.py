import asyncio
from aiotractive import Tractive
from DataConvertors.Influx.LocationHistory import LocationHistory
from DataWriters.InfluxDBWriter import InfluxDBWriter
import datetime

class TractiveHistoryPosition:
    def __init__(self, config):
        self.tracker_id = config['tracker_id']
        self.influx_bucket = config['influx_bucket']
        self.tractive_mail = config['tractive_mail']
        self.tractive_pass = config['tractive_pass']
        self.last_sec = config['last_sec']

    async def process_data(self):
        now = datetime.datetime.now().timestamp()
        time_from = now - int(self.last_sec)
        time_to = now
        data = await self.get_data_from_tractive(time_from, time_to)
        self.write_data_to_influx(data)

    async def get_data_from_tractive(self, time_from, time_to):
        async with Tractive((self.tractive_mail), self.tractive_pass) as client:
            tracker = client.tracker(self.tracker_id)
            return await tracker.positions(time_from, time_to, "json_segments")

    def write_data_to_influx(self, data):
        influx_writer = InfluxDBWriter()
        for entry in data[0]:
            location_entry = LocationHistory(entry, self.tracker_id).get_point()
            influx_writer.write_to_influx(location_entry, self.influx_bucket)
