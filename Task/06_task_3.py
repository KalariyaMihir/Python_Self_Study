# WAF to find the factorial of n


def factorial(numb):

    fact = 1

    for ind in range(1,numb+1):

        
        fact *= ind
    print(f"Factorial of {numb} is : {fact}")



number = int(input("Enter a Number : "))
factorial (number) 

