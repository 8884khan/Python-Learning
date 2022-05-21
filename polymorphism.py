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
