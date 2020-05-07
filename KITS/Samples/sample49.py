
import time

is_dst = time.daylight and time.localtime().tm_isdst > 0
print(is_dst)
print(time.tzname[is_dst])
