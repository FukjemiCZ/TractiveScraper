import json
from influxdb_client import Point

# LocationHistory(data).get_point()
class LocationHistory:
    def __init__(self, data, _id):
        data = json.loads(json.dumps(data))
        time = int(data['time'] * 1000000000)
        self.point = Point(_id)
        self.point.tag("tracker", _id)
        self.point.tag("sensor_used", data['sensor_used'])
        self.point.time(time)
        self.point.field("latitude", data['latlong'][0])
        self.point.field("longitude", data['latlong'][1])
        self.point.field("altitude", data['alt'])
        self.point.field("speed", data['speed'])
        self.point.field("course", data.get('course', None))
        self.point.field("pos_uncertainty", data['pos_uncertainty'])

    def get_point(self):
        return self.point
