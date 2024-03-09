# Practice of strings function

str = "My Name is Mihir"
str2  = "my name is mihir"

print(str.endswith("i")) # endswith function returns true if string ends/match with given string

print(str2.capitalize()) # Capital the First word of string
print(str2) # it only capitalize temporary

# To modified the string permanently
str2 = str2.capitalize()
print(str2)

print(str.replace("Name is" , "Self")) #Replace the string with substring

print(str.find("Mihir")) #find index of given substring

print(str.count("i")) # returns counts of substring


