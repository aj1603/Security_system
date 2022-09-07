# import datetime
# import time

# e = datetime.datetime.now()

# # print ("Current date and time = %s" % e)

# # print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
# first_time = ("%s:%s:%s" % (e.hour, e.minute, e.second))
# print (first_time)
# second_time = ("%s:%s:%s" % (e.hour, e.minute, e.second))
# print (second_time)

# from datetime import datetime

# birthday = datetime(2022, 9, 6, 12, 55, 0)
# diff = datetime.now() - birthday
# print (diff)




# from datetime import date, time

# def get_difference(date1, date2):
#     delta = date2 - date1
#     return delta.days

# d1 = date(2021, 10, 20)
# d2 = date(2022, 2, 20)

# d3 = time(12, 10, 5)
# d4 = time(10, 2, 6)

# times = get_difference(d3, d4)
# print(f'Difference is {times} days')

# days = get_difference(d1, d2)
# print(f'Difference is {days} days')



# import time

# start_time = time.time()

# def countdown(t): 
#     """
#     Countdown Timer
#     """
#     while t:
#         # Divmod takes only two arguments so
#         # you'll need to do this for each time
#         # unit you need to add
#         mins, secs = divmod(t, 60) 
#         hours, mins = divmod(mins, 60)
#         days, hours = divmod(hours, 24)
#         timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs) 
#         print(timer, end="\r" )
#         time_before_sleep = time.time() - start_time
#         time.sleep(1) 
#         time_after_sleep = time.time() - start_time
#         print(timer, time_before_sleep, time_after_sleep)
#         t -= 1
        
#     print('Fire in the hole!!') 

# t = 100

# countdown(int(t))

import threading
import datetime
e = datetime.datetime.now()

def gfg():
	print("GeeksforGeeks\n")

timer = threading.Timer(8.0, gfg)
print(e)
timer.start()
print("Exit\n")
print()
