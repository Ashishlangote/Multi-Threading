from time import sleep
from threading import Thread


def upload():
    print("Uploading Video on server started")
    sleep(5)
    print("Video Uploading Done")


def sendNotificationToSubscribers():
    print("Sending Notification Of Video Uploading To All Subscriber")


t1 = Thread(target=upload)
t2 = Thread(target=sendNotificationToSubscribers)

t1.start()
t1.join()
t2.start()
