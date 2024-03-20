# Practice of static method

class Employee:
    
    def __init__(self):
        print("Hello")
    
    @staticmethod
    def show():
        return("Hello Students")

emp = Employee()
print(emp.show())
     
    