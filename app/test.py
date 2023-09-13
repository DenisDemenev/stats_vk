import datetime
import time
date_now_datatime = datetime.datetime.now()
date_now = time.time()

print(date_now_datatime)
print(int(date_now - date_now_datatime.timestamp()))
