# WAF to find in which line of the file does the word "learning" occur first.
# Print-1 if word not found

def print_line():
    word = "Programming"
    
    with open ("practice.txt","r") as file:
        line = 1

        data = True

        while data:

            data = file.readline()

            if(word in data):
                return(word ,"Found on line no :",line) 
            line += 1

    return -1

print(print_line())