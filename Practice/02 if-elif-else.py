# Practice of If elif and else (conditional statement)

signal = "Yellow"

if(signal == "Red"):
    print("Stop Vehicle")

elif(signal == "Green"):
    print("Go")

elif(signal == "Yellow"):
    print("Slow Your Vehicle") # tabular space in the start of line call's indentation
    print("Wait until signal get's Green")

else :
    print("Signal isn't working")