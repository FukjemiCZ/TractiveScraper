import json
from influxdb_client import Point

# HwInfo().get_point(data)
class HwInfo:
    def __init__(self, data):
        data = json.loads(json.dumps(data))
        time = int(data['time'] * 1000000000)
        self.point = Point(data["_id"])
        self.point.tag("tracker", data["_id"])
        self.point.tag("hw_status", data['hw_status'])
        self.point.tag("power_saving_zone_id", data['power_saving_zone_id'])
        self.point.tag("_type", data['_type'])
        self.point.tag("_version", data['_version'])
        self.point.tag("report_id", data['report_id'])
        self.point.time(time)
        self.point.field("clip_mounted_state", data['clip_mounted_state'])
        self.point.field("battery_level", data['battery_level'])

    def get_point(self):
        return self.point