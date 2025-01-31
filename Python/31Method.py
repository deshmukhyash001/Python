'''Method Overriding'''
class Diploma:
    def get_diploma(self):
        print('I got Diploma')

class CO(Diploma):
    def get_diploma(self):
        print("I am with Co diploma")
    
class IF(Diploma):
    def get_diploma(self):
        print("I am with IF diploma")
    
co_dip = CO()
co_dip.get_diploma()

#I am with Co diploma

class Animal:
    def breathe(self):
        print("I breathe Oxygen")
    def feed(self):
        print("I eat food")
    
class Herbivorous(Animal):
    def feed(self):
        print("I only eat Plants. I am Vegetarian")

class Carnivorous(Herbivorous):
    def feed(self):
        print("I only eat mass. I am Non - Vegetarian")

Herbi = Herbivorous()
Herbi.feed()
Herbi.breathe()
Carni = Carnivorous()
Carni.feed()
Carni.breathe()
#Methods will be overwritten on each other and only last method will be called

'''Method Overloading'''
class A:
    def __init__(self,a,b=None) -> None:
        self.a = a
        self.b = b
    
    def printA(self):
        if self.b is None:
            print("Hi Camel")
        else:
            print("Hi Mammel")

objA = A(4,6)
objA.printA()
objA2 = A(4)
objA2.printA()   