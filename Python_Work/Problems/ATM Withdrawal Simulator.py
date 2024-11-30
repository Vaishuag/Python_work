
# ATM Withdrawal Simulator

Cur_bal=int(input("Enter Your Current Ballance:"))
Withdraw=int(input("Enter the amount to withdraw:"))

if(Withdraw > Cur_bal):
    print("Insufficient Balance")

elif(Withdraw % 100 ==0):
    Balance = Cur_bal - Withdraw
    print("Transaction is Successful.\nYour new balance is",Balance)

else:
    print("Invalid amount.\nPlease enter a multiple of 100.")
    























































        
