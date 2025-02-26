#author: George
#date: 2025-02-05
#description: This is a simple program to test the george module

# import the time module
import time

GEORGE = True
i=0
while GEORGE:
    print(i)
    i+=1
    if i%10==0:
        print("      GEORGE")
    time.sleep(0.001)


