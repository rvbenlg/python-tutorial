import time

seconds_since_epoch = time.time()

print(time.ctime(seconds_since_epoch))  # now

time_object = time.localtime()
format = "%B %d %Y %H:%M:%S"  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
local_time = time.strftime(time_object)
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d, %B, %Y")
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
