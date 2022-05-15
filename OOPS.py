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

print("------------------------------------------------")

class Student:
    def __init__(self,n,m):
        self.name = n
        self.marks = m
    def display(self):
        print("Name = ",self.name,"Marks= ",self.marks)
    def grade(self):
        if self.marks >= 75:
            print("First grade")
        elif self.marks >=50:
            print("Sencod class")
        elif self.marks >=35:
            print("Third class")
        else:
            print("Failed")
n = int(input("Enter the number of Students:- "))
for i in range(n):
    name = input("Enter Student name:- ")
    marks = int(input("Enter the marks:- "))
    s=Student(name,marks)
    s.display()
    s.grade()
    
    

