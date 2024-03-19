number = [12, 75, 150, 180, 145, 525,50]

for num in number:

    if(num % 5 == 0):

        if(num > 150):
            if(num > 500):
                break
            continue
            
        print(num)