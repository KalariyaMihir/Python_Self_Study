# WAP to find the sum of first n numbers.(using while)

number = int(input("Enter number : "))

sum = 0

i = 1
while i <= number:
    sum +=i
    i += 1

print(sum)
