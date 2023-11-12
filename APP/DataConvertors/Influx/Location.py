import json
from influxdb_client import Point

# Location(data).get_point()
class Location:
    def __init__(self, data):
        data = json.loads(json.dumps(data))
        time = int(data['time'] * 1000000000)
        self.point = Point(data["_id"])
        self.point.tag("tracker", data["_id"])
        self.point.tag("sensor_used", data['sensor_used'])
        self.point.tag("pos_status", data['pos_status'])
        self.point.tag("power_saving_zone_id", data['power_saving_zone_id'])
        self.point.tag("_type", data['_type'])
        self.point.tag("_version", data['_version'])
        self.point.tag("report_id", data['report_id'])
        self.point.tag("nearby_user_id", data['nearby_user_id'])
        self.point.time(time)
        self.point.field("latitude", data['latlong'][0])
        self.point.field("longitude", data['latlong'][1])
        self.point.field("speed", data['speed'])
        self.point.field("pos_uncertainty", data['pos_uncertainty'])
        self.point.field("altitude", data['altitude'])

    def get_point(self):
        return self.point
