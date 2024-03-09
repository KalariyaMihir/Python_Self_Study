# Print the multiplication table of number n.

i = 1
table = int(input("Enter Table Number : "))

while i <= 10:
    print(f"{table} * {i} = {table*i}")
    i += 1

print(f"Table of {table} is Ended.")