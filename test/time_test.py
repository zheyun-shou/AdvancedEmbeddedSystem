import time
import copy
from interval import Interval

now = time.localtime(time.time())

now_localtime = time.strftime("%H:%M:%S", now)  #是一个str
now_next = copy.deepcopy(now)
now_next.tm_min = now_next.tm_min +
now_next.tm_sec = 0

now_nextlocaltime = time.strftime("%H:%M:%S", now_next)
