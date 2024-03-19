# Practice of file write

# f = open("myfile.txt","a")

# f.write("\nHitesh can't dance sala")

# f.close()

# ------------------------------------------------------------

# file = open("myfile.txt","r+")

# file.write("My name is Mihir")

# print(file.read())

# file.close()

# ------------------------------------------------------------

with open("D:\Full Stack\BE\Python shardha\Practice\sample.txt","r") as f:

    print(f.read())

with open("D:\Full Stack\BE\Python shardha\Practice\sample.txt", "w" ) as f:
    f.write("New Data")


