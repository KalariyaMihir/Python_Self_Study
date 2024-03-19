# Practice of Contractor
class Student:
    def __init__(self,fullname,agee):
        self.name = fullname
        self.age = agee
        
        print("Adding new Student in Database...")
        
name = input("Enter Student's Name : ")
age = int(input("Enter Student's Age : "))
s1= Student(name,age)
print(s1.name)
print(s1.age)

name = input("Enter Student's Name : ")
age = int(input("Enter Students Age : "))
s2 = Student(name,age)
print(s2.name)
print(s2.age)
