# Multiple Inheritance

class Father:
    def __init__(self):
        super().__init__()      # Calling Parent Constructor
        print("Father class Constructor")
    def show(self):
        print("Father Class Method")

class Mother:
    def __init__(self):
        super().__init__()      # Calling Parent Constructor
        print("Mother class Constructor")
    def showM(self):
        print("Mother Class Method")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()      # Calling Mother and Father Constructor
        print("Son class Constructor")
    def showS(self):
        print("Son Class Method")

s = Son()
s.show()
s.showM()