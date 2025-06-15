import schedule
import time

def teju():
    print("jay ganesh")

schedule.every(2).seconds.do(teju)

if __name__ == "__main__":
    while True:
    
        schedule.run_pending()
        time.sleep(0.2)
