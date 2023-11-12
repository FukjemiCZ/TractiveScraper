import asyncio
from config import get_env_LocationHistory
from DataScrapers.HistoryPosition import TractiveHistoryPosition
from ErrorHandling.ConsoleLogger import ConsoleLogger

console_logger = ConsoleLogger()

if __name__ == "__main__":
    console_logger.log_info("Start LocationHistory processing...")
    try:
        tractive_config = get_env_LocationHistory()
        tractive_processor = TractiveHistoryPosition(tractive_config)
        asyncio.run(tractive_processor.process_data())
        console_logger.log_info("LocationHistory processing completed successfully.")
    except Exception as e:
        console_logger.log_error(f"Error during LocationHistory processing: {e}")
        print(f"Error: {e}")
        import sys
        sys.exit(1)
