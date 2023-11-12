# Environment Variables:
- `INFLUX_URL`: URL of the InfluxDB server.
- `INFLUX_ORG`: InfluxDB organization name (e.g., primary).
- `INFLUX_TOKEN`: Token for accessing InfluxDB.
- `TRACTIVE_MAIL`: Tractive account email.
- `TRACTIVE_PASSWORD`: Tractive account password.
- `TRACTIVE_TRACKER`: Tracker ID for Tractive.
- `LAST_SEC`: Time window for data retrieval from Tractive in seconds (e.g., 36000).
- `INFLUX_BUCKET_SCRAPER_HISTORYPOSITION`: InfluxDB bucket for storing history position data from Tractive (e.g., Tractive).
- `SCHEDULE_SCRAPER_HISTORYPOSITION`: Schedule interval for scraping history position data (in minutes).
- `INFLUX_BUCKET_SCRAPER_HWINFO`: InfluxDB bucket for storing hardware info data.
- `SCHEDULE_SCRAPER_HWINFO`: Schedule interval for scraping hardware info data (in minutes).

# Usage:
```bash
docker run -d \
-e INFLUX_URL=[[insert url here]] \
-e INFLUX_ORG=primary \
-e INFLUX_TOKEN=[[insert token here]] \
-e TRACTIVE_MAIL=[[insert mail here]] \
-e TRACTIVE_PASSWORD=[[insert pass here]] \
-e TRACTIVE_TRACKER=[[insert TrackerID here]] \
-e LAST_SEC=36000 \
-e INFLUX_BUCKET_SCRAPER_HISTORYPOSITION=Tractive \
-e SCHEDULE_SCRAPER_HISTORYPOSITION=[[insert int in minutes here]] \
-e INFLUX_BUCKET_SCRAPER_HWINFO=hw_info \
-e SCHEDULE_SCRAPER_HWINFO=[[insert int in minutes here]] \
fukjemicz/tractivescraper:latest
```
