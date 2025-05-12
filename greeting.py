import time

timestamp = time.strftime('%H:%M:%S')
#print(timestamp)
hr = int(time.strftime('%H'))
#print(hr)
min = time.strftime('%M')
#print(min)
sec = time.strftime('%S')
#print(sec)

if (hr < 12):
    print(f"Good Morning! the time is {timestamp}")
elif (hr >= 12 and hr < 16):
    print(f"Good Afternoon! the time is {timestamp}")
elif (hr >= 16 and hr < 20):
    print(f"Good Evening! the time is {timestamp}") 
else:
    print(f"Good Night! the time is {timestamp} and its time to go to bed!")