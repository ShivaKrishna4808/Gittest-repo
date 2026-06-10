# multiple 

class universe:
    def universeMethod(self):
        print("I am in the Universe")

class earth(universe):
    def eathMethod(self):
        print("I am on Earth")
    
class India(earth):
    def IndiaMethod(self):
        print("I am in India")

person = India()

person.universeMethod()
person.eathMethod()
person.IndiaMethod()