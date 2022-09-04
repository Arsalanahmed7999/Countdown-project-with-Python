import time
# STEPS - 
#1 make a countdown function and take t(time) as an input
# 2 Now create a while loop until t is greater than 0
# 3 now subtract time by 1
# 4 Now use time.sleep() function which happen after each seconds since given an input of 1
# 5 now take seconds as an input and put the countdown duration
# 6 Now make a use of error handling in a case where a user do put an integer value
# 7 Now convert the seconds into integer since the input default value is string.
# 8 now call back the function and your project is ready.

def countdown(t):
    while t>0:
        t-=1
        time.sleep(1) #sleep(1) -> seconds(1)
        print(t)
    print('Time is up')
seconds = input('Enter the duration of a countdown: \n')

while not seconds.isdigit():
    print('Error !! Enter an integer value only')
    seconds = input('Enter the duration of a countdown: \n')
seconds = int(seconds)
countdown(seconds)