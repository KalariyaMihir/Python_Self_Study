# WAP to check if a list contains a palindrome of elements.


# ---------------- my logic ----------------

# number = [ 1, 2, 3, 2, 1]

# if (number == number.reverse):
#     print("list is Palindrome")

# else:
#     print("List is Palindrome")


# ---------------- shardha's logic ----------------

# pal = ['m', 'a', 'a', 'm']
pal = [1, 2, 3]


cpy = pal.copy()
cpy.reverse()

if(cpy == pal ):
    print("Palindrome")

else:
    print("Not Palindrome")
