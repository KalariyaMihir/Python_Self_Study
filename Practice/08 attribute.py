# Practice of class Attribute & Object Attribute

class Student :

    # school_name and name is attribute of class   
    school_name = "M.G.E.C."
    name = "None"

    def __init__(self,name,age,marks):
        # self.name, self.age, self.marks are attribute of objects
        self.name = name
        self.age = age
        self.marks = marks

st_1 = Student("Mihir",22,98.43)
print("\n\b",st_1.name,st_1.age,st_1.marks,Student.school_name,"\n")

st_2 = Student("Bhagirath",20,87.14)
print(st_2.name,st_2.age,st_2.marks,Student.school_name,"\n")

st_3 = Student("Hitesh",21,89.78)
print(st_3.name,st_3.age,st_3.marks,Student.school_name,"\n")

st_4 = Student(Student.name,20,85.12)
print(st_4.name,st_4.age,st_4.marks,Student.school_name)



        