from threading import *
from time import sleep

obj = Semaphore()


def greet(message):

    obj.acquire()

    for i in range(3):
        print(message)

    sleep(3)
    obj.release()


t1 = Thread(target=greet, args=("Hello 1",))
t2 = Thread(target=greet, args=("Hello 2",))
t3 = Thread(target=greet, args=("Hello 3",))
t4 = Thread(target=greet, args=("Hello 4",))

t1.start()
t2.start()
t3.start()
t4.start()