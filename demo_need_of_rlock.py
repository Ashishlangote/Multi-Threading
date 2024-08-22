from threading import *
from time import sleep

#objLock = Lock()
objRLock = RLock()

def get_first_line():
    objRLock.acquire()
    print("Code to get first line from text file")
    objRLock.release()

def get_second_line():
    objRLock.acquire()
    print("Code to get second line from text file")
    objRLock.release()

def combine():
    objRLock.acquire()
    get_first_line()
    get_second_line()
    objRLock.release()


t1 = Thread(target=combine)
t1.start()

""""
Note: Creating Object by Lock Class and because of some situation of codes if we have to do
      multiple times uses of acquire & release method then code execution will not take place
      so, avoid that problem RLock technique is introduce. 

Rlock: This technique allow us to use multiple time of acquire and release method in our program.
       It is used to avoid race condition and makes code smooth execution

"""