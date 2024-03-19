# WAF to find given number is odd or even

def find(num):
    
    if(num%2 == 0):
        print(f"{num} is Even")
    
    else:
        print(f"{num} is Odd")

print("Program to find number is Even or Odd")

value = int(input("Enter Number : "))

find(value)

