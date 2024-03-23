# Practice of private Private Attribute

# Private Attribute meant to be inside the Class and it doesn't work outside the class

class Bank:
    
    def __init__(self,name,pas) :
        
        self.name = name
        self.__pas = pas
        
    def __show(self):
        print("Hello User")

    def prnt(self):
        self.__show()
        
b = Bank("Mihir",5454)

print(b.name)

print(b.prnt())        