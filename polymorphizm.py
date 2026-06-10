# polymorphizm = 1 obj performs muliptle opers

class Duck:
    def sound(self):
        return "Quack,quack!"
    
class anotherbird:
    def sound(self):
        return "I'm similar to a Duck"
    
def makesound(Duck):
    print(Duck.sound())


duck = Duck()
anotherBird = anotherbird()

makesound(duck)

makesound(anotherBird)


