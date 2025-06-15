import schedule
import time
from datetime import datetime

def tej():
    print(f"namskar  —  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

schedule.every().day.at("09:00").do(tej)

if __name__ == "__main__":
    tej()

    while True:
        schedule.run_pending()   
        time.sleep(1)        
