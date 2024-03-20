# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# get odd number from list1 and e even number from list2 and create a new list of those numbers output should be [25,35,40,60,90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

# ---------------------------------------------------- Logic 1 -------------------------------------------------------

for n in list1:
    if(n %2 == 0):
       pass
    else:
        list3.append(n)
        
for n in list2:
    if(n%2 == 0):
        list3.append(n)
        

print(list3)


# ------------------------------------------------------ Logic 2 -------------------------------------------------------
# list3 = list1[2::2]+list2[0::2]

# print(list3)

