# Reverse the given number

n=int(input("Enter the Number:"))

reverse_no=0

while(n>0):
    r=n%10  # to get last digit

    n=n//10     # remove last digit

    reverse_no= reverse_no*10+r
print("The reverse of Number is: ",reverse_no)
