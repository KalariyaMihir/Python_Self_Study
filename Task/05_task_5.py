# Search for a number x in this tuple using loop

numbers= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)

print("Select number to find an index : 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25")
num = int(input("Enter Number : "))

idx = 0

length = len(numbers)-1

while idx <= length:
    if(numbers[idx] == num ):
        print(f"Fonded on idex {idx}")

    else:
        print("Searching...")
    
    idx += 1