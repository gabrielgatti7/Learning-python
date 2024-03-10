import time

print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                         epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time()), end='\n\n')  # current date


time_object = time.localtime()  # local time
print(time_object)
# time_object = time.gmtime()     # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time, end='\n\n')


time_string = "26 January, 2024"
time_object = time.strptime(time_string, "%d %B, %Y")   # parse a string representation of a
#                                                               time and/or date and return a time object
print(time_object, end='\n\n')


# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string, end='\n\n')

# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_seconds = time.mktime(time_tuple)
print(time_seconds)