# Practice of method in dictionary 


nested = {
    "Name" : "Mihir Kalariya",
    "Standard" : 5,
    "subjects" : ["Gujarati", "Hindi", "Maths", "Science", "English", "Sanskrit"],
    "Marks" : {
        "Gujarati" : 67,
        "Hindi" : 56,
        "Maths" : 53,
        "Science" : 68,
        "English" : 65,
        "Sanskrit" : 67
    },
}


# key method 
# it returns the key of dictionary

# print(nested)
# print(nested.keys())
# print(list(nested.keys()))
# print("\n\n")



# value method
# it returns the values of dictionary 

# print(nested.values())
# print("\n\n")



# items method

# pairs = list(nested.items())
# print(pairs[3])
# print("\n\n")



# get method

# print(nested["Name2"])
# print(nested.get("Name2"))
# print("\n\n")



# update method

update = {"Result" : True,
           "City" : "Rajkot",
           "Name" : "Mihir"}

nested.update(nested)

print(nested)


