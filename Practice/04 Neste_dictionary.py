# Practice of nested dictionary

nested = {
    "Name" : "Hitesh Boricha",
    "Standard" : 5,
    "subjects" : ["Gujarati", "Hindi", "Maths", "Science", "English", "Sanskrit"],
    "Marks" : {
        "Gujarati" : 21,
        "Hindi" : 25,
        "Maths" : 3,
        "Science" : 18,
        "English" : False,
        "Sanskrit" : 27
    },
    "Result" : False  
}

print(nested["Name"])
print("English", nested["Marks"]["English"])