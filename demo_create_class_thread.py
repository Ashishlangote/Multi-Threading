# Create thread: by using thread class present in threading module
from threading import Thread, current_thread
''''
class Demo:
    def greet(self):
        print(f"t1 thread details:{current_thread()}")
        for i in range(5):
            print("Hello")

d = Demo()
t1=Thread(target=d.greet)
t1.start()

print(f"Main thread details:{current_thread()}")
for i in range(4):
    print("Hi")

'''
# create thread: by extending & inheriting thread class
from time import sleep
from threading import Thread

list_of_videos_to_uplpoad =["Basics of Python.mp4","Basics of Django.mp4","Basics of DS.mp4"]

class MyTestThread(Thread):
    def __init__(self):
        print("I am Constructor")
        super().__init__()
        # Thread.__init__(self)
    def run(self):
        for videoId in list_of_videos_to_uplpoad:
            print(f"Started Uploading video - {videoId}")
            sleep(5)
            print(f"Upload {videoId} successfully")

t1 = MyTestThread()
t1.start()

for i in range(3):
    sleep(0.5)
    print(" Copyrights Checking")
