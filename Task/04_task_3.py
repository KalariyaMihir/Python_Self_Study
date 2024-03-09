# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as values.

marks = {}

marks.update(
 
 {"Science" : input("Enter Marks of Science : "),
  "Maths" : input("Enter Marks of Maths : "),
  "English" : input("Enter marks of English : ")}
)

print(marks) 

