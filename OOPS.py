#instance variable
class demo:
    def __init__(self):
        self.x =10
    def fun(self):
        self.y = 20
ob = demo()
ob.fun()
ob.z =30
print("x=",ob.x)
print("y=",ob.y)
print("z=",ob.z)

print("==================================")


#static variable
class demo:
    x =10 #static variable
    def __init__(self):
        self.y = 20 #instance variable
ob1=demo()
ob2=demo()
print("ob1 values=",ob1.x,ob1.y)
print("ob2 values= ",ob2.x,ob2.y)
print(id(ob1))
print(id(ob2))
print(demo.x)
ob1.y = 111
print("ob1 values=",ob1.x,ob1.y)
print("ob2 values= ",ob2.x,ob2.y)


print("=====================")

# static and a class method
from datetime import date
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def frombirthdate(cls,name,age):
        return cls(name,date.today())
    @staticmethod
    def isAdult(age):
        return age>18
p1 = person("shahbaz",30)
p2 = person.frombirthdate("shahbaz",1992)
print(p1.age)
print(p2.age)



