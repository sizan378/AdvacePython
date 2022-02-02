# Constructor Overriding 

class Father:   # Parent Class
    def __init__(self):
        self.money = 1000
        print("Parent Class Instructor", self.money)

    def show(self):
        print("Parent Class Instance Mehtod")

class Son(Father):
    def __init__(self):
        super().__init__()      # Calling Parent Class Construtor
        # self.money = 2000
        # self.car = 'CAR'
        print("Son class Constructor")
    def disp(self):
        print("Child Class Instructor Mehtod", self.money)


c = Son()