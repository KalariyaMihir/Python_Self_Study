# WAF to print sum of n natural number using recursion

def cal(value):


    if(value == 0 ):
        return 0
    
    return cal(value-1) + value

sum = cal(5)

print(sum)



