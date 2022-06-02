#abstract emthod

from abc import *
class Demo:
    @abstractmethod
    def m(self):
        pass
class child(Demo):
    def m(self):
        print("hello world")
ob = child()
ob.m()
   
    
    
print("----------------------------------------------------")

print("EXAMPLE 2")

from abc import *
class Demo(ABC):
    @abstractmethod
    def m1(self):
        pass
    
    def m2(self):
        print("non abstract method")
class child(Demo):
    def m1(self):
        print("abstract method")
c =child()
c.m1()
c.m2()

