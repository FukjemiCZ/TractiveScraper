import re
import schedule
import time
import subprocess
import os
import sys

from APP.ErrorHandling.ConsoleLogger import ConsoleLogger

def run_Scraper_HistoryPosition():
    try:
        console_logger.log_info("Starting LocationHistory...")
        result = subprocess.run(["python3", "app/LocationHistory.py"], stderr=subprocess.PIPE)
        result.check_returncode()
        console_logger.log_info("LocationHistory executed successfully.")
    except subprocess.CalledProcessError as e:
        console_logger.log_error(f"Error running LocationHistory: {e}")
        sys.exit(1)

def run_Scraper_HwInfo():
    try:
        console_logger.log_info("Starting HwInfo...")
        result = subprocess.run(["python3", "app/HwInfo.py"], stderr=subprocess.PIPE)
        result.check_returncode()
        console_logger.log_info("HwInfo executed successfully.")
    except subprocess.CalledProcessError as e:
        console_logger.log_error(f"Error running HwInfo: {e}")
        sys.exit(1)

min_shp = int(os.getenv('SCHEDULE_SCRAPER_HISTORYPOSITION'))
min_shi = int(os.getenv('SCHEDULE_SCRAPER_HWINFO'))

# Configure custom logging
console_logger = ConsoleLogger()

console_logger.log_info("Starting TractiveScraper")
console_logger.log_info(f"Scraper HistoryPosition run every {min_shp} minutes")
console_logger.log_info(f"Scraper HwInfo run every {min_shi} minutes")

# Set up tasks that run every X minutes
schedule.every(min_shp).minutes.do(run_Scraper_HistoryPosition)
schedule.every(min_shi).minutes.do(run_Scraper_HwInfo)

# Loop to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
