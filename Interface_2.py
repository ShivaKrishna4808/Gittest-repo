class demoInterface:
    def displaymsg(self):
        pass

class newClass(demoInterface):
    def displaymsg(self):
        print("This is my Message")

obj = newClass()
obj.displaymsg()