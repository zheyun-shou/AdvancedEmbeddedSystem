import copy
import datetime
import time
from interval import Interval

now_ori = datetime.datetime.now()
nextmin = copy.deepcopy(now_ori)
nextmin = nextmin.replace(minute=now_ori.minute+1)
nextmin = nextmin.replace(second=0)
nextmin = nextmin.replace(microsecond=0)
now_localtime = nextmin.strftime('%H:%M:%S')
print(now_localtime)
print(type(now_localtime))
#print(type(now_localtime))

#print(today)

#print(type(today))



while True:

    realnow = datetime.datetime.now()
    # if realnow.second == 59:
    #     realnow = realnow.replace(minute= realnow.minute )
    #     realnow = realnow.replace(second= 0)
    realnow_localtime = realnow.strftime('%H:%M:%S')
    realnow_time = Interval(realnow_localtime, realnow_localtime)

    time_interval = Interval(now_localtime, now_localtime)

    #print(time_interval)

    if realnow_time in time_interval:
        print("是在这个时间区间内")
        print("要执行的代码部分")