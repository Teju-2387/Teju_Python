import schedule
import time

def teju():
    print("Do coding")

schedule.every(3).seconds.do(teju)

if __name__ == "__main__":
    while True:
    
        schedule.run_pending()
        time.sleep(0.3)
