from threading import Thread, current_thread
import os


def greet():
    # print(f"Thread Name: {current_thread().name()}")
    print("Hi All")


def sayHello():
    # print(f"Thread Name: {current_thread().name()}")
    print("Hello")


t1 = Thread(target=greet, name="MyT1")
t2 = Thread(target=sayHello, name="MyT1")

# TID prints None because thread id is created after calling t1.start()
# print(f"TID of T1={t1.ident}")
# print(f"TID of T2={t2.ident}")

t1.start()
t2.start()

print(f"TID of T1={t1.ident}")
print(f"TID of T2={t2.ident}")

print("*********Get Thread Name************")
print(t1.name)
print(t2.name)

# print("*********Get Thread Name*************")
# print(t1.getName())
# print(t2.getName())

print("*********Name to Thread***************")
t1.name = "T-ABC"
t2.name = "T-PQR"

# print("***********Name to Thread**************")
# t1.setName("T-ABC")
# t2.setName("T-PQR")

print(t1.name)
print(t2.name)

print("**************Print Id of Threads**********")
print(t1.ident)  # Id is given by Python Interpreter
print(t1.native_id)  # Id is giver by Operating System

print(t1.ident)
print(t1.native_id)

print("********************************************")

print(current_thread().name)
# print(current_thread().getName())
current_thread().name = "MyMainThread"  # MainThread name can be changed
print(current_thread().name)
# print(current_thread().getName())
print(current_thread().ident)
print(current_thread().native_id)

print("*********************************************")

print(f"Process ID = {os.getpid()}")
