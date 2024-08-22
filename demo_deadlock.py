from threading import *

Lock1 = Lock()
Lock2 = Lock()


def thread_1():
    print("Thread 1 acquiring Lock1...")
    Lock1.acquire()
    print("Thread 1 acquired Lock1")

    print("Thread 1 acquiring Lock2...")
    Lock2.acquire()
    print("Thread 1 acquired Lock2")


def thread_2():
    print("Thread 2 acquiring Lock2...")
    Lock2.acquire()
    print("Thread 2 acquired Lock2")

    print("Thread 2 acquiring Lock1...")
    Lock1.acquire()
    print("Thread 2 acquired Lock1")


t1 = Thread(target=thread_1)
t2 = Thread(target=thread_2)

t1.start()
t2.start()
