# Multipliction of Digits

n=int(input("Enter the Numbers: "))
org=n
multiple_of_no=1

while(n>0):
    digit=n%10
    multiple_of_no = multiple_of_no * digit
    n=n//10
print("The multiple of ",org,'is',multiple_of_no)
