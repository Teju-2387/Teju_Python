import schedule
import time
from datetime import datetime

def write_time_once():

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("demo.txt", "a") as f:
        f.write(timestamp + "\n")
    print(f"[{timestamp}]  →  wrote to Demo.txt")
    return schedule.CancelJob 


schedule.every(1).minutes.do(write_time_once)

if __name__ == "__main__":
    print("Scheduler started — will write to Demo.txt in 5 minutes…")
    while True:
        schedule.run_pending()
        if not schedule.jobs:         
            break
        time.sleep(0.2)
