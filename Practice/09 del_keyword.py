# Practice of del keyword
# used to delete object properties or object it self

class Student:
    
    def __init__(self,name):
        self.name = name

s1 = Student("Mihir")

print(s1.name)
del s1.name
print(s1.name)
    
