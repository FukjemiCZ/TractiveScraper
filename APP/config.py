import os

def get_env_LocationHistory():
    return {
        'tracker_id': os.getenv('TRACTIVE_TRACKER'),
        'tractive_mail': os.getenv('TRACTIVE_MAIL'),
        'tractive_pass': os.getenv('TRACTIVE_PASSWORD'),
        'influx_bucket': os.getenv('INFLUX_BUCKET_SCRAPER_HISTORYPOSITION'),
        'last_sec': os.getenv('LAST_SEC'),
    }

def get_env_HwInfo():
    return {
        'tracker_id': os.getenv('TRACTIVE_TRACKER'),
        'tractive_mail': os.getenv('TRACTIVE_MAIL'),
        'tractive_pass': os.getenv('TRACTIVE_PASSWORD'),
        'influx_bucket': os.getenv('INFLUX_BUCKET_SCRAPER_HWINFO'),
    }
