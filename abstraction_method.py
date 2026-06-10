from abc import ABC, abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    def method2(self):
        print("concrete method")

class concreteclass(democlass):
    def method1(self):
        super().method1()
        return
    
obj1 = concreteclass()
obj1.method1()
obj1.method2()