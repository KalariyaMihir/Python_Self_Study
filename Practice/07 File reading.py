# Practice of file i/o
# Reading the file

file = open("myfile.txt","r")
data = file.read()
print(data)
# print(type(data))

line_1 = file.readline()
print(line_1)

line_2 = file.readline()
print(line_2)



file.close()    



