'''
polymorphism:-

'''

#Duck Typing
class Duck:
    def talk(self):
        print("Quack....Quack")
class Cat:
    def talk(self):
        print("Meow Meow")
class Dog:
    def talk(self):
        print("Bow ....Bow")
def fun(ob):
    ob.talk()
cat = Duck()
fun(cat)


print("++++++++++++++++++++++++")
#concatination 2 referance variable using magic methods
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
ob1 = Book(100)
ob2 = Book(50)
print(ob1+ob2)
