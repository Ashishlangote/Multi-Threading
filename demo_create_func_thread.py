

# 1] Import Thread Class
from threading import Thread, current_thread
import datetime 
from time import sleep


# 2] Create a function
def greet():
    for i in range(5):
        print("Hi All")

def sayHi():
    for  i in range(3):
      print("Hi")

def sayHello():
    print("Hello")


# 3] Create Object of Thread Method
t1 = Thread(target=greet)
t2 = Thread(target=sayHi)
t3 = Thread(target=sayHello)


startTime = datetime.datetime.now()
# 4] Call Start Method
# t1.start()
# t2.start()
# t3.start()  

greet()
sayHi()
sayHello()

endTime = datetime.datetime.now()

print(f"Start Time:{startTime}")
print(f"Start Time:{endTime}")

exicutionTime = endTime - startTime
print(exicutionTime)

# Parametrise Function :
# 1) positional & non keyword agruement

from threading import Thread
import datetime

def greet(n, greet_msg):
    for i in range(n):
        print(greet_msg)

def func(*param):
    for i in (param):
        print(i)

param = ["Suraj","Satish","Shashi","Ankit","Ashish"]
t1 = Thread(target=greet, args=(9, "Good Morning")) 
t2 =  Thread(target=func, args=(param))

t1.start()
t2.start()

# keyword argument:

from threading import Thread, current_thread
import datetime

def greet(n, greet_msg):
    print(f"t1 Thread details: {current_thread()}")
    for i in range(n):
        print(greet_msg)


def func(**var):
    print(f"t2 Thread details: {current_thread()}")
    for i in var.items():
        print(i)

var = {"name":"Suraj","sirname":"Rathod","dist":"Washim","taluka":"karanja","gaon":"wadgaon"}
t1 = Thread(target=greet, kwargs={"n":5,"greet_msg":"Good Evening"})
t2 = Thread(target=func,kwargs=var)

t1.start()
t2.start()

print(f" Main Thread details: {current_thread()}")
for i in range(5):
    print("Hi All")



