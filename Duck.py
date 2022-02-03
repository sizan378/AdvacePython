# Duck Typing

class Duck:
    def walk(self):
        print("Thapak Thapak Thapak")
class Horse:    
    def walk(self):
        print("Tabdak tabdak Tabdak")

def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)


# Strong Typing

class Duck:
    def walk(self):
        print("Thapak Thapak Thapak")
class Horse:
    def walk(self):
        print("Tabdak tabdak Tabdak")
class Cat:
    def talk(self):
        print("Meow Meow Meow")

def myfunction(obj):
    if hasattr(obj, 'walk'):  # Strong Typing 
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()

d = Duck()
myfunction(d)

c = Cat()
myfunction(c)