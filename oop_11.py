'''Python datetime
In this article, you will learn to manipulate date and time in 
Python with the help of examples.
Python has a module named datetime to work with dates and times. 
Let's create a few simple programs related to date and time before we dig deeper.'''

# Example 1: Get Current Date and Time
# import datetime
# print(dir(datetime.datetime))
# print(datetime.datetime.now())
# x=datetime.datetime.now()
# print("Todays time and dates are:",x)
# Example 2: Get Current Date                                                                         
# import datetime
# print("Todays date is:",datetime.date.today())

# Commonly used classes in the datetime module are:

# date Class
# time Class
# datetime Class
# timedelta Class

# datetime.date Class
# Example 3: Date object to represent a date
# import datetime
# print(datetime.date(2020,7,1))
# print(datetime.datetime.today())
# from datetime import date
# print(date(2020,7,1))

# # Example 4: Get current date
# from datetime import date
# print(date.today())

# Example 5: Get date from a timestamp
# from datetime import date
# print(date.fromtimestamp(1593549645.0))

# from datetime import date as timestamp
# print(timestamp.fromtimestamp(13012210010))

# Example 6: Print today's year, month and day
# from datetime import date
# print(date.today().year)
# print(date.today().month)
# print(date.today().day)

# Example 7: Time object to represent time
# from datetime import time 
# a=time() #hour=0 min=0 sec=0
# print("a=",a)

# a=time(2,35,34) 
# print("a=",a)

# datetime.datetime
# Example 9: Python datetime object
# from datetime import datetime
# a=datetime(2020,7,1,2,40,45)
# print(a)
# Example 10: Print year, month, hour, minute and timestamp
# print(a.year)
# print(a.month)
# print(a.day)
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.timestamp())
# datetime.timedelta
# Example 11: Difference between two dates and times
# from datetime import datetime,date
# t1=date(year=2020,month=7,day=1)
# t2=date(year=2021,month=12,day=12)
# t3=t2-t1
# print(t3,type(t3))

# Example 12: Difference between two timedelta objects
# from datetime import timedelta
# t1=timedelta(weeks=2,days=5,hours=4,minutes=34)
# t2=timedelta(weeks=3,days=3,hours=3,minutes=35)
# t3=t2-t1
# print(t3,type(t3))

# Example 13: Printing negative timedelta object
# from datetime import timedelta
# t1=timedelta(seconds=33)
# t2=timedelta(seconds=56)
# t3=t1-t2
# print(t3)
# print(abs(t3))
# Example 14: Time duration in seconds
# from datetime import timedelta
# t=timedelta(days=2,hours=4,minutes=45,seconds=45)
# print(t.total_seconds())

# strpttime()
#strfttime()
# from datetime import datetime
# print(datetime.now())

# print(datetime.now().strftime("%H:%M:%S"))
# print(datetime.now().strftime("%d/%m/%Y"))
# print(datetime.today().strftime("%b"))  
# print(datetime.now().strftime("%B"))
# print(datetime.now().strftime("%a"))
# print(datetime.now().strftime("%A"))  
# %a=day ,%b=month
# print(datetime.now().strftime("%I"))
# %I=12 hours clock time
# print(datetime.now().strftime("%I %p"))
# %p=local am/pm time
# print(datetime.now().strftime("%f"))
# %f = microsecond 
# print(datetime.now().strftime("%x"))
# print(datetime.now().strftime("%X"))
# %x=local's appropriate date and %X=local's appropriate time
# print(datetime.now().strftime("%c"))
# print(datetime.now().strftime("%C"))
# %c= local time and date  
# %C = last digit of the year 
# print(datetime.now().strftime("%U"))
# print(datetime.now().strftime("%j"))

# using datetime finding execution time of a time
# from datetime import datetime
# p=datetime.today()
# n=int(input("Enter the last digit:"))
# sum=(n*(n+1))/2
# print("Sum=",sum)
# q=datetime.today()
# print(q-p) 
# from datetime import datetime
# r=datetime.today()
# # n=int(input("Enter the last digit:"))
# sum_1=0
# for i in range(0,n+1):
#     sum_1+=i
# print("Sum=",sum_1)
# s=datetime.today()
# print(s-r) 

# python time module 
# time.time()
# import time
# seconds=time.time()
# print(seconds)

# time.ctime()
# import time 
# seconds=1593756271.8245046
# print(time.ctime(seconds))

# time.asctime()
# import time
# print(time.asctime())

