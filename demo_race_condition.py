from threading import Thread
from time import sleep

number = 50

def add(no):
    global number
    sleep(1)
    number = number + no
    print(number)

def subtract(no):
    global number
    sleep(1)
    number = number - no
    print(number)

t1 = Thread(target=add,args=(5,))
t2 = Thread(target=subtract, args=(10,))

t1.start()
#t1.join()     # To avoid race condition use thread.join()
t2.start()