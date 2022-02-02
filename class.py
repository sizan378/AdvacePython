# Class Create
class Myclass():
    def show(self):
        print("Hello sizan")

x = Myclass()
x.show()

# Constructor Create
class Mobile():
    # Constructor Without Parameter
    def __init__(self):
        self.model = 'Realme'

    def show_model(self):
        print("Model",self.model)

relme = Mobile()
relme.show_model()

# Constructor Create With Parameter m adn v

class Mobile:
    # Constructor
    def __init__(self,m,v=80): # v is a default Value
        self.model = m
        self.volumn = v
    # Create another Method
    def show_model(self,p):
        price = p
        print("Model:",self.model, "price:",price)
        print("Volumn:",self.volumn)

realme = Mobile('Realme C17',6654)
realme.show_model(20000)