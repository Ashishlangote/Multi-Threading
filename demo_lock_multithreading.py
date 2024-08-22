from threading import *
from time import sleep

objLock = Lock()

def greet(objLock,message):
    
    objLock.acquire()  # To avoid the race condition

    # Below for loop is creatical section
    for i in range(5):
        print(message)
    sleep(5)
    objLock.release()   # To avoid the race condition

t1 = Thread(target=greet, args=(objLock,'Hi All'))
t2 = Thread(target=greet, args=(objLock,'Hello ALL'))

t1.start()
t2.start()

""""
Lock technique: It is a Thread synchronization technique which is used to avoid race conditon in code
                It does not allow multple uses of acquire & release method in a programe 

"""