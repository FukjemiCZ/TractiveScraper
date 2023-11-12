import asyncio
from config import get_env_HwInfo
from DataScrapers.HwInfo import TractiveHwInfo

if __name__ == "__main__":
    print("HwInfo_start")
    try:
        tractive_config = get_env_HwInfo()
        tractive_processor = TractiveHwInfo(tractive_config)
        asyncio.run(tractive_processor.process_data())
        print("HwInfo_done")
    except Exception as e:
        print(f"Error: {e}")
        import sys
        sys.exit(1)