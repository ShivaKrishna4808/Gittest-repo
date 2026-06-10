# Static method

class employee:
    empcount = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        employee.empcount+=1

    def showcount():
        

        print(employee.empcount)
        return
    counter = staticmethod(showcount)

e1 = employee("Bhavana",24)
e2 = employee("Rajesh",26)
e3 = employee("shiva",25)

e1.counter()
employee.counter()



