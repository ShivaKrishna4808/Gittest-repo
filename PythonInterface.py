from abc import ABC,abstractmethod

class demoInterface(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract Method1")
        return
    @abstractmethod
    def method2(self):
        print("Abstract Method2")
        return
    


class concreteclass(demoInterface):
    def method1(self):
        print("This is Method1")
        return
    
    def method2(self):
        print("This is method2 ")
        return
    
obj = concreteclass()

obj.method1()
obj.method2()


# test driven