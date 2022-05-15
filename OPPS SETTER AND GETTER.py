#GETTER AND SETTER 
class Student:
    def setter1(self,n):
        self.name=n
    def setter2(self,m):
        self.marks = m
    def getter1(self):
        return self.name
    def getter2(self):
        return self.marks

n =int(input("Enter no of  students:- "))
for i in range(n):
    name =input("Enter the name of student:- ")
    marks =int(input("Enter the marks:- "))
    s=Student()
    s.setter1(name)
    s.setter2(marks)
    print(s.getter1())
    print(s.getter2())
