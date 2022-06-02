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
    
