import time
import os

def shutDown(time):
    while time != -1:
        print(f"Minus {time} seconds left to shutdown.")
        time-=1
        if (time == 0):
            os.system("shutdown /p")
            

shutDown(10)