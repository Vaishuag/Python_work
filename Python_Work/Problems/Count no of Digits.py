# Count no of Digits
n=int(input("Enter the numbers: "))
count=1

while(n>10): # check the didvided value is lesser than 10
    n=n//10
    count=count+1
print("The count is:",count)
