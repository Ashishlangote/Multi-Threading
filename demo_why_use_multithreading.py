from time import sleep
import time
from threading import Thread

def addition(no1, no2):
    print(f"Addition Of {no1} and {no2}")
    sleep(1)
    print(f"Addition Of {no1} + {no2} = {no1+no2}")


def subtraction(no1, no2):
    print(f"Subtraction Of {no1} and {no2}")
    sleep(1)
    print(f"Subtraction Of {no1} - {no2} = {no1-no2}")

'''
start_time = time.time()
addition(15,5)
subtraction(15,5)
'''
# Epoch - Second form Point say 1 Jan 2000 till now
start_time = time.time()

t1 = Thread(target=addition, args=(15,10))
t2 = Thread(target=subtraction, args=(15,10))

t1.start()
t1.join()
t2.start()

print(f"Total Time Of Execution = {time.time() - start_time}")
