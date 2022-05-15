class Demo:
    a  =10
    def __init__(self):
        Demo.b = 20
        print(Demo.b)
    def fun1(self):
        Demo.c=30
        print(Demo.c)
    @classmethod
    def fun2(cls):
        Demo.d = 40
        cls.e =60
        print(Demo.d)
        print(cls.e)
    @staticmethod
    def fun3():
        Demo.f = 70
        print(Demo.f)
print(Demo.a)
ob = Demo
ob.fun1()
ob.fun2()
ob.fun3()
print(Demo.__dict__)



# Error in line 21 please help 
