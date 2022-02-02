class Father:
    def __init__(self):
        print("Father Class Constructor")
    def show(self):
        print("Father Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()      # Calling Father Constructor
        print("Son Class Constructor")
    def disp(self):
        print("Son Class Method")

class Grandson(Son):
    def __init__(self):
        super().__init__()      # Calling Son Constructor
        print("Grandson Class Constructor")
    def dispp(self):
        print("GrandSon Class method")

g = Grandson()

g.disp()
g.dispp()
g.show()