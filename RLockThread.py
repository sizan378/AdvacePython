# RLock Method Apply

from threading import Thread, current_thread, RLock

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        print("Lock",self.l)
    def reserve(self, need_seat):
        self.l.acquire()
        print("Aquire",self.l)
        print("Available Seats:", self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print("Sorry! All seats has alloted")

        self.l.release()
        print("Release",self.l)

f = Flight(4)
t1 = Thread(target=f.reserve, args=(1,), name="sizan")
t2 = Thread(target=f.reserve, args=(1,), name="Mahmud")
t3 = Thread(target=f.reserve, args=(1,), name="sizan1")
t4 = Thread(target=f.reserve, args=(1,), name="Mahmud1")
t1.start()
t2.start()
t3.start()
t4.start()