# Practice of Super Key word

class Car:
    
    def __init__(self,type):
        
        self.type = type
        
    @staticmethod
    def start():
        print("Car Start...")
        
    @staticmethod
    def off():
        print("Car Stopped.")

class Toyota(Car):
    def __init__(self,name, type):

        self.name = name
        super().start()
        super().__init__(type)
        
cr = Toyota("Fortuner", "Hybrid")
print(cr.name,cr.type)