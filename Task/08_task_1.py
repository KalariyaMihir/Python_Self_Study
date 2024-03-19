# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average.


class Student :
    
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks 
        
    def average(self):
        sum = marks1 + marks2 + marks3
        
        avg = sum / 3
        
        return(f"\nAverage of {name} is : {avg}")
        



name = input("Enter Student's Name : ")

marks1 = int(input("Marks of Subject 1 : "))
marks2 = int(input("Marks of Subject 2 : "))
marks3 = int(input("Marks of Subject 3 : "))
marks=[marks1,marks2,marks3]

s1 = Student(name,marks)

print(s1.average())
# print(s1.name,s1.marks)


    
                  