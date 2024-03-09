# Practice of Dictionary in Python

# dictionary create the dictionary of multiple variables of multiple data type (it's like an object)
# it comes in pair or key and value  
# we can also store the list and tuple 
# key can also be an integer, float, boolean, or list and tuple also
# dictionary is unordered, mutable and don't allows the duplicate keys 

dictionary = {
    "name" : "Mihir Kalariya",
    "course" : "Full-Stack Python",
    "age" : 22,
    "fees" : 90000,
    "Technology" : ("Front-End", "Back-End"),
    "Front-End" : ["HTML", "CSS", "Bootstrap", "JS", "jQuery", "ReactJS"],
    "Back-End" : ["Python", "Django"]
}

dictionary["name"] = "Hitesh"
dictionary["time"] = "1 Year"

print(type(dictionary))
print(dictionary)

