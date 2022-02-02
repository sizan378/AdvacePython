#Instance Variabel
class Mobile:
    def __init__(self):  # Constractor
        self.model = 'Real Me' # Instance Variable
    def show_model(self):   # Instance Method
        print(self.model)   # Accessing Instance Variable

realmi = Mobile()
realmi.show_model()
print(realmi.model)

#Without Parameter Class Method
class MobilePhone():
    @classmethod            #  Decoretor
    def show_model(cls):    # Class Method
        print('ReaMe X')

relme = MobilePhone()
MobilePhone.show_model()    # Calling Class Method

# Class Variable Create

class Mobile:
    fp = 'Yes'              # Class Variable
    @classmethod
    def show_model(cls, p): # Class Method with Parameter/Formal Argumetn
        cls.price = p
        print('Fingerprint', cls.fp,'Price:',cls.price)

realme = Mobile()
realme.show_model(2540)


# Static Method with Parameter
class Mobile:
    @staticmethod           #Decorator
    def show_model(m, p):   # Static Method
        model = m
        price = p
        print("Model:",model,"price:",price)
relme = Mobile()
relme.show_model("sizan Reame C17",1254)