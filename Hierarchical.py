# Hierarchical Inheritance
class Father:
    def showF(self):
        print("Father class mehtod")

class Son(Father):
    def showS(self):
        print("Son class method")

class Daughter(Father):
    def showD(self):
        print("Daughter class Mehtod")

d = Daughter()
d.showD()
d.showF()

s = Son()
s.showS()
