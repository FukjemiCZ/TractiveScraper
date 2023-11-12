import asyncio
from config import get_env_HwInfo
from DataScrapers.HwInfo import TractiveHwInfo
from ErrorHandling.ConsoleLogger import ConsoleLogger

# Configure custom logging
console_logger = ConsoleLogger()

if __name__ == "__main__":
    console_logger.log_info("Start HwInfo processing...")
    try:
        tractive_config = get_env_HwInfo()
        tractive_processor = TractiveHwInfo(tractive_config)
        asyncio.run(tractive_processor.process_data())
        console_logger.log_info("HwInfo processing completed successfully.")
    except Exception as e:
        console_logger.log_error(f"Error during HwInfo processing: {e}")
        print(f"Error: {e}")
        import sys
        sys.exit(1)
