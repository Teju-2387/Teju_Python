import schedule
import time
from datetime import datetime

def lunch_time():
    print(f"Lunch time!:{datetime.now():%Y-%m-%d %H:%M:%S}")

def wrap_up():
    print(f"Wrap up!:{datetime.now():%Y-%m-%d %H:%M:%S}")

schedule.every().day.at("13:00").do(lunch_time)   # 1 p.m.
schedule.every().day.at("18:00").do(wrap_up)      # 6 p.m.

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
