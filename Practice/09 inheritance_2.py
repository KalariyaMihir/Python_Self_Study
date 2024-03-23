# Practice of Multiple Inheritance  

class A:
    a = "A"
    
class B:
    b = "B"
    
class C(A,B):
    c = "C"
    
obj = C()

print(obj.a)