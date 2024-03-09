# Find larger number from 4 numbers

one = int(input("Enter First Number : "))
second = int(input("Enter Second Number : "))
third = int(input("Enter Third Number : "))
fourth = int(input("Enter Fourth Number : "))

if((one > second and one > third) or (one > fourth)):
    print(one,"is the largest number.")

elif(second > third and second > fourth):
    print(second,"is the Largest Number")

elif(third > fourth):
    print(third,"is the Largest Number")

else:
    print(fourth,"is the Largest Number")
