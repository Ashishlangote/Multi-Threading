import threading
print("Hello Suraj")
print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.current_thread().is_alive)

