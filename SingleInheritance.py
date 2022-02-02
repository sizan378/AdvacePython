# Single Inheritance

class Father:
    money = 2000 # Class Variable

    def show(self):
        print("Parent Class Insatance Method")
    
    @classmethod
    def showmoney(cls):
        print("Parent class Method price:", cls.money)

    @staticmethod
    def static():
        a = 50
        print("Parent Class Statice Method:", a)

class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

s = Son() # Child class Called
s.disp() # Child Method Call

s.show()  # Parent Class Method call
s.showmoney()
s.static()


# Constructor in Inheritance

class Parent:
    def __init__(self):
        self.money = 1000
        print(" Parent Class Money:", self.money)

    def show(self):
        print("Parent Class show")

class Child(Parent):
    def disp(self):
        print("show Child class display", self.money)

c = Child()
c.disp()
c.show()
    