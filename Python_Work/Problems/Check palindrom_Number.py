# To check the no is Palindrom

n=int(input("Enter the Numbers: "))

org_nu=n
rev_no=0

while(n>0):
    digit=n%10  # to get last digit of the numbers

    rev_no = rev_no * 10 + digit #print no in reverse

    n=n//10

if ( org_nu == rev_no ):
    print( org_nu, " is Palindrom")
else:
    print( org_nu, " is not a Palindrom")
