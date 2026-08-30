import re
from datetime import datetime

pattern=r"12:\d{2}:\d{2}"
times=[]
datetimes=[]
with open("logs/errors.log",'r')as file:
    lines=file.readlines()
    for line in lines:
        result=re.findall(pattern,line)
        times.extend(result)

first_error = datetime.strptime(times[0], "%H:%M:%S")
#print(first_error)
last_error = datetime.strptime(times[-1], "%H:%M:%S")
#print(last_error)
total_time=(last_error-first_error).total_seconds()
#print(total_time)
intervals=len(times)-1
average=total_time/intervals
print(average)

