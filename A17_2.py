import schedule
import time
from datetime import datetime

def show_datetime():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

schedule.every(1).minutes.do(show_datetime)

if __name__ == "__main__":

    show_datetime()

    while True:
        schedule.run_pending()
        time.sleep(0.5)         
