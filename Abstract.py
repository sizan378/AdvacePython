# Abstract Class Create

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print('Concrete Method')

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defination Abstract Class")

A = Child()
# A.disp()
# A.show()

class DefenceForce(ABC):
    def area(self):
        pass
    def Gun(self):
        print("Gun = AK47")

class Army(DefenceForce):
    def area(self):
        print("Army_Area = Land")

class Navy(DefenceForce):
    def area(self):
        print("Navy_Area = Sea")

class Air(DefenceForce):
    def area(self):
        print("Air_Area = Sky")

a = Army()
a.area()
a.Gun()
print()
af = Air()
af.area()
af.Gun()
print()
n = Navy()
n.area()
n.Gun()