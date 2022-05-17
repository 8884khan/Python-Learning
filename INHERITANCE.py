# sinle inheritance
class A:
    def m1(self):
        print("First")
class B(A):
    def m2(self):
        print("First and sencond")
cc = B()
cc.m1()
cc.m2()

print("=================================")

#multi level ingeritance
class A:
    def m1(self):
        print("First")
class B(A):
    def m2(self):
        print("First and sencond")
class C(B):
    def m3(self):
        print("First,Second and Third")
ob = C()
ob.m1()
ob.m2()
ob.m3()
print("===================================")
#multipple Inheritance another example
class A:
    def m(self):
        print("parent1")
class B:
    def m(self):
        print("Parent 2")
class C(B,A):
    pass
cc = C()
cc.m()



class A:
    def m(self):
        print("parent1")
class B:
    def m(self):
        print("Parent 2")
class C(A,B):
    pass
cc = C()
cc.m()

