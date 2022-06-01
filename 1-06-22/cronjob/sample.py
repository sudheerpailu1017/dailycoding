from datetime import datetime
import time

now=datetime.now()
print("Python Script Started :",now.strftime("%H:%M:%S"))
i=1
while i<=5:
    now=datetime.now()
    print("Working on task(s){task_num} of 5 at {time_now}...".format(task_num=i,time_now=now.strftime("%H:%M:%S")))
    time.sleep(5)
    i=i+1
    
print("Job Completed:", now.strftime("%H:%M:%S"))
