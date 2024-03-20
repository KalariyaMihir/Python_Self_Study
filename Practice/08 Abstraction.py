# Practice of Abstraction

# Abstraction is Hiding the implementation details of a class and only showing essential features to the user.  

class Car:
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True 
        self.acc = True 
        print("Wroom... Wromm..")


cr = Car()
cr.start()

    
