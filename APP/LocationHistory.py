import asyncio
from config import get_env_LocationHistory
from DataScrapers.HistoryPosition import TractiveHistoryPosition

if __name__ == "__main__":
    print("start")
    try:
        tractive_config = get_env_LocationHistory()
        tractive_processor = TractiveHistoryPosition(tractive_config)
        asyncio.run(tractive_processor.process_data())
        print("done")
    except Exception as e:
        print(f"Error: {e}")
        import sys
        sys.exit(1)