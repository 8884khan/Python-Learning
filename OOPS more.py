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
        cls.e =50
        print(Demo.d)
        print(cls.e)
    @staticmethod
    def fun3():
        Demo.f = 60
        print(Demo.f)
print(Demo.a)
ob = Demo
ob.fun1(30)
ob.fun2()
ob.fun3()
print(Demo.__dict__)

# change argument and got answer but when run i am not getting the value 20 


# another way 
class Demo:
    a  =10
    def __init__(self):
        Demo.a = 20
        print(Demo.a)
    def fun1(self):
        Demo.a=30
        print(Demo.a)
    @classmethod
    def fun2(cls):
        Demo.a = 40
        
        print(Demo.a)
      
    @staticmethod
    def fun3():
        Demo.a = 60
        print(Demo.a)
print(Demo.a)
ob = Demo
ob.fun1(30)
ob.fun2()
ob.fun3()
print(Demo.__dict__)


print("-----------------------------------------------")

class Demo:
    def add(self,x=None,y=None,z=None):
        if x!=None and y!=None and z!=None:
            print("Sum = ",x+y+z)
        elif x!=None and y!=None:
            print("sum= ",x+y)
        else:
            print("pgm is to add 3 nos ... provide atlest 2 values")
d = Demo()
d.add(10,20,30)
d.add(20,50)
d.add()

print("---------------------------------------------------")

class Demo:
    def add(self,*x):
        sum = 0;
        for i in x:
            sum = sum+i
        print(sum)
d = Demo()
d.add(10,20,30)
d.add(20,10)
d.add(10)


