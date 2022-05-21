#Operator Over Loading
class Student:
    def __init__(self,name,marks):
        self.name =name
        self.marks = marks
    def __gt__(self,other):
        return self.marks > other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __eq__(self,other):
        return self.marks==other.marks
s1 = Student("Shahbaz marks= ",85)
s2 = Student("Khan marks= ",87)

if s1>s2:
    print("Higher Marks",s1.name)
elif s1<s2:
    print("Higher marks= ",s2.name)
else:
    print("Equal Marks")
