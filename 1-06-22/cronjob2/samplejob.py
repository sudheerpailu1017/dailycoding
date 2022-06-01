import schedule
from datetime import datetime
import time

def samplejob():
    now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    fp=open(now+'.txt',"x")


schedule.every(10).seconds.do(samplejob)
while True:
    schedule.run_pending()
    time.sleep(1)
