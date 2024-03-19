# From a file containing numbers separated by comma, print the count of even numbers. 

with open("number.txt","r") as f:
    data = f.read()
    
    number = data.split(",")
    print(number)
    
    for ind in number:
        if(int(ind) % 2 == 0):
            print(ind)
        