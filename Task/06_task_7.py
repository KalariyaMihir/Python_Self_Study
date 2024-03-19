# Write a recursive function to print all elements of list

cars = ["Alto" , "Swift", "Nano", "Thar"]

def elements(elm,ind=0):
    
    if(ind == len(elm)):
        return 0
    
    print(elm[ind])
    elements(elm,ind+1)

elements(cars)