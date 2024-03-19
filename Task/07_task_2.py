# WAF to replace occurrence of "Java" with "Python" in above file.

with open("Practice.txt","r") as f:

    data = f.read()

    print(data)
    new = data.replace("Java","Python")


with open("Practice.txt","w") as f:

    f.write(new)