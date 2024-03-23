# Practice of Class method

class Person:
    
    name = "None"
    
    # class method changes the attribute of class
    @classmethod
    def changeName(cls,name):
        cls.name = name
        
        
p = Person()

p.changeName("Mihir")
print(p.name)

print(Person.name)

