# Practice of Recursion

def recursion(num):
    if(num == -1):
        return
    print(num)
    recursion(num-1)

recursion(5)