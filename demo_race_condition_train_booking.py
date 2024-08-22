from threading import *

objRLock = RLock()

class TrainTicketBooking:

    def __init__(self, name, available_seats, lock_obj):

        self.train_name = name
        self.available_seats = available_seats
        self.lock_obj = lock_obj

    def reserveSeats(self, number_of_seats_book):
        
        self.lock_obj.acquire()
        self.lock_obj.acquire()
        print(f"Current Available Seats = {self.available_seats}")

        if  self.available_seats >= number_of_seats_book:
            
            current_thread_name = current_thread().name
            # Actual Ticket Booking Code and Upadating database
            print(f"{number_of_seats_book} reserved for {current_thread_name}")
            self.available_seats -= number_of_seats_book
        
        else:
            print(f"No seats are available for booking in Train = {self.train_name}")
        
        self.lock_obj.release()
        self.lock_obj.release()

train1 = TrainTicketBooking("Deccan Express", 10, objRLock)

t1 = Thread(target=train1.reserveSeats,args=(1,),name="Mr.ABC")
t2 = Thread(target=train1.reserveSeats,args=(2,),name="Mrs.PQR")
t3 = Thread(target=train1.reserveSeats,args=(5,),name="Miss.XYZ")
t4 = Thread(target=train1.reserveSeats,args=(6,),name="Mr.LMN")

t1.start()
#t1.join()
t2.start()
#t2.join()
t3.start()
t4.start()

t4.join() # Here join method used beacause given below code should be executed after t4 thread 

print(f"Current Available Seats = {train1.available_seats}")
            

