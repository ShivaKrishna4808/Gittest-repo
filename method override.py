class parent:
    def myMethod(self):
        print("Calling parent method")

class child(parent):
    def myMethod(self):
        print("Calling child method")

c = child()
c.myMethod()