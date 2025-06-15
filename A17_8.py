import schedule
import time
from datetime import datetime

def check_email():
    print(f"Checking email…  {datetime.now():%Y-%m-%d %H:%M:%S}")

schedule.every(10).seconds.do(check_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(0.20)          
