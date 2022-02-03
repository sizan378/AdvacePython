# Method Overriding

class Add:
    def result(self, a,b):
        print("Addintion:",a+b)

class Multi(Add):
    def result(self, a,b):
        super().result(30,40)           # Calling Parent Class Method
        print("Multipication:", a*b)

m = Multi()
m.result(10,20)