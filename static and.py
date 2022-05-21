# to call parent class static method to child class static method

class P:
    @staticmethod
    def m():
        print("Static Method")
class C(P):
    @staticmethod
    def m4():
        super().m()
ob = C()
ob.m()
    
