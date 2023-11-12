import schedule
import time
import subprocess
import os
import sys

min_shp = int(os.getenv('SCHEDULE_SCRAPER_HISTORYPOSITION'))
min_shi = int(os.getenv('SCHEDULE_SCRAPER_HWINFO'))

def run_Scraper_HistoryPosition():
    # Run the tractive.py script using subprocess
    result = subprocess.run(["python3", "app/LocationHistory.py"], stderr=subprocess.PIPE)
    if result.returncode == 1:
        error_output = result.stderr.decode('utf-8') if result.stderr else "Error output missing"
        print(f"Error: Subprocess LocationHistory exited with return code 1. Error output: {result.stderr.decode('utf-8')}")
        sys.exit(1)

def run_Scraper_HwInfo():
    # Run the tractive.py script using subprocess
    result = subprocess.run(["python3", "app/HwInfo.py"], stderr=subprocess.PIPE)
    if result.returncode == 1:
        error_output = result.stderr.decode('utf-8') if result.stderr else "Error output missing"
        print(f"Error: Subprocess HwInfo exited with return code 1. Error output: {result.stderr.decode('utf-8')}")
        sys.exit(1)

# Set up tasks that run every X minutes
schedule.every(min_shp).minutes.do(run_Scraper_HistoryPosition)
schedule.every(min_shi).minutes.do(run_Scraper_HwInfo)

# Loop to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
