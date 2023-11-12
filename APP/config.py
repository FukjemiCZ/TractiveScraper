import os
from ErrorHandling.ConsoleLogger import ConsoleLogger

# Configure custom logging
console_logger = ConsoleLogger()

# Configure logging

def get_env_LocationHistory():
    console_logger.log_info("Retrieving LocationHistory configuration...")
    try:
        tracker_id = os.getenv('TRACTIVE_TRACKER', None)
        tractive_mail = os.getenv('TRACTIVE_MAIL', None)
        tractive_pass = os.getenv('TRACTIVE_PASSWORD', None)
        influx_bucket = os.getenv('INFLUX_BUCKET_SCRAPER_HISTORYPOSITION', None)
        last_sec = os.getenv('LAST_SEC', None)

        if None in (tracker_id, tractive_mail, tractive_pass, influx_bucket, last_sec):
            console_logger.log_error("One or more required environment variables for LocationHistory are missing.")
            raise ValueError("One or more required environment variables for LocationHistory are missing.")

        return {
            'tracker_id': tracker_id,
            'tractive_mail': tractive_mail,
            'tractive_pass': tractive_pass,
            'influx_bucket': influx_bucket,
            'last_sec': last_sec,
        }
    except Exception as e:
        console_logger.log_error(f"Error retrieving LocationHistory configuration: {e}")
        raise

def get_env_HwInfo():
    console_logger.log_info("Retrieving HwInfo configuration...")
    try:
        tracker_id = os.getenv('TRACTIVE_TRACKER', None)
        tractive_mail = os.getenv('TRACTIVE_MAIL', None)
        tractive_pass = os.getenv('TRACTIVE_PASSWORD', None)
        influx_bucket = os.getenv('INFLUX_BUCKET_SCRAPER_HWINFO', None)

        if None in (tracker_id, tractive_mail, tractive_pass, influx_bucket):
            console_logger.log_error("One or more required environment variables for HwInfo are missing.")
            raise ValueError("One or more required environment variables for HwInfo are missing.")

        return {
            'tracker_id': tracker_id,
            'tractive_mail': tractive_mail,
            'tractive_pass': tractive_pass,
            'influx_bucket': influx_bucket,
        }
    except Exception as e:
        console_logger.log_error(f"Error retrieving HwInfo configuration: {e}")
        raise
