# Create Single Tasking Thread

from threading import Thread
from time import sleep

class MyExm:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Question 1 Solved")
        sleep(3)
    def q2(self):
        print("Question 2 Solved")
        sleep(5)
    def q3(self):
        print("Question 3 Solved")
        sleep(2)


mye = MyExm ()
t =  Thread(target=mye.solve_question)
t.start()