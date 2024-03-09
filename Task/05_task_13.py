# WAP to find the factorial of first n numbers.

number = int(input("Enter Number : "))

fact = 1

for idx in range(1, number+1):

    fact *= idx

print(f"Factorial of {number} is {fact}.")