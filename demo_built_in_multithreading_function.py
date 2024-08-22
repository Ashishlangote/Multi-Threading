from threading import Thread, current_thread, main_thread, get_native_id, active_count, enumerate

def greet():
    print(f"TID of Thread 1 = {current_thread().ident}")
    print(f"Native ID of Thread 1 = {get_native_id()}")
    print("Hi All")

def sayHello():
    print(f"TID OF Thread 2 = {current_thread().ident}")
    print(f"Native ID of Thread = {get_native_id()}")    
    print("Hello")

t1 = Thread(target=greet)
t2 = Thread(target=sayHello)


print("**********Print Active Count******************")

print(f"Active Count 1 = {active_count()}")
t1.start()
print(f"Active Count 2 = {active_count()}")
t2.start()
print(f" Active Count 3 = {active_count()}")
'''
print("**********Print thread is alive****************")

print(f"Does Thread t1 is alive = { t1.is_alive()}")
t1.start()
print(f"Does Thread t1 is alive = {t1.is_alive()}")

print(f"Does Thread t2 is alive = {t2.is_alive()}")
t2.start()
print(f"Does Thread t2 is alive = {t2.is_alive()}")

print("************************************************")
'''
print(current_thread())
print(main_thread())

print(f"Active Count = {active_count()}")
print(f"List of Running Thread is {enumerate()}")