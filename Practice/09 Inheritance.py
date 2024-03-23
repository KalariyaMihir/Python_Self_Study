# Practice of Inheritance

class Car:
    
    @staticmethod
    def on():
        return("Car is Start...")
        
    @staticmethod
    def off():
        return("Car is Off.")
        
class Brand(Car):
    
    def __init__(self, brand):
        self.brand = brand 
        
        

class Model(Brand):
    
    def  __init__(self,name):
        self.name = name
 
car = Model("Safari")

print(car.brand)

print(car.on())


         
    