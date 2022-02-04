from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child Class")
        print("Defining Abstract Method")

class GrandChild(Child):
    def disp2(self):
        print("Grand Child Class")
        print("Defining Abstract Method")



gc = GrandChild()
gc.disp2()
gc.disp1()