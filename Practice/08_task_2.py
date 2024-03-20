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
            return None
            
        else:
            db_amount =  self.bln - amount
            return(db_amount)
    

ac = Account(23165135465,98000)
print(ac.ac_no)
        
print(ac.debit())