# print the multiplication table of a number n 

table = int(input("Enter Number to Print an Table : "))

print(f"\nTable of {table} is ->\n")
for num in range(1 ,11):
    print(f"{table} * {num} = {table * num}")
