# Search if word "learning" exits in the file or not. 

with open ("practice.txt","r") as file:

    data = file.read()

    if "learning" in data:
        print("\nYes...")
        print("I have Found word 'learning in the string'.")
    else:
        print("Not Found the Word...")