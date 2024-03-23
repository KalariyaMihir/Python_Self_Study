# Create account class with 2 attribute - balance & account no.
# create methods for debit, credit & printing the balance

class Account :
    
    def __init__(self,acount_no,balance):
        
        self.ac_no = acount_no
        self.bln = balance
        
    def debit(self):
        amount = int(input("Enter Withdraw Amount : "))
        if(amount > self.bln):
            print(" !!! Warning ")
            print("Inefficient Balance")
            return ''
            
        else:
            db_amount =  self.bln - amount
            return(f"{db_amount} Balance in your Acount {self.ac_no}")
        
    def credit(self):
        amount = int(input("Enter Deposit Amount : "))
        
        if(amount > 700000):
            print("You have Reached the Limit")
            print("You can't Deposit more then 700000 at Once")
        else:
            db_amount = self.bln + amount
            return(f"{amount} is credited in your account {self.ac_no} Total Balance is {db_amount}")
        
    
ac_number = int(input("Enter Your Account Number : "))
 
ac = Account(ac_number,98000)

        
print("Enter 'withdraw' for Debit and 'Deposit' for Credit ")
choice = input("Enter Your Choice :  ")

if(choice == "Withdraw" or choice == "withdraw"):
    print(ac.debit())

elif(choice == "Deposit" or choice == "deposit"):
    print(ac.credit())
        