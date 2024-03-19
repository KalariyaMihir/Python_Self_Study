# WAF to convert USD to INR 

def conv(us):
    i = 82.91
    rupee = us * i 
    print(f"{us} Dollars = {rupee} Indian Rupees.")

    return(rupee)



value = int(input("Enter Dollars to convert in rupees : "))

conv(value)
    