# Search for a numbers X in this tuple using loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
choice = 49
idx = 0

length = len(numbers)

for num in numbers:

    if(num == choice):
        print(f"Found {choice} on index {idx}.")

    idx += 1

