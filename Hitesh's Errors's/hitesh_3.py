# find prime number on users input

sn = int(input("Enter Starting Number : "))
en = int(input("Enter Ending Number : "))

for n in range(sn,en+1):
    
    if(n > 1):
        for num in range(2,n):
            if(n % num == 0):
                break
        else:
            print(n)
