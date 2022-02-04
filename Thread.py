# Thread Create

import imp
# from threading import Thread
from threading import Thread, current_thread

def disp(a):
    print("Thread is running",a)

t = Thread(target=disp, args=(10,))
t.start()

def show():
    print("Child Thread Object", current_thread().getName())

t = Thread(target=show)
t.start()

print("Main Thread Name", current_thread().getName())

print()
print()
print()

# class Mythread(Thread):
#     def run(self):
#         print("Run Method")
# t = Mythread()
# t.start()
# print(t.name)

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Run Method")
t = Mythread()
t.start()
t.join()
for i in range(5):
    print("Main Thread")

class ThreadClass(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Thread Constructor")

    def run(self):
        pass
t = ThreadClass()
t.start()
print("Main Thread", current_thread().getName())
print()

# Create Thread Class without using Child Class

class ChildClass:
    def disp(self, a,b):
        print(a,b)

myt = ChildClass()

t = Thread(target=myt.disp, args=(10,20))
t.start()