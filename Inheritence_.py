# Singel Inheritence 
# parent and child 

class Parent:
    def parentMethod(self):
        print("Calling parent methods")

class Child(Parent):
    def childMethod(self):
        print("Calling child Method")

c = Child()
c.childMethod()
c.parentMethod()


