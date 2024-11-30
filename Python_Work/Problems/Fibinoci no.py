n=int(input('Enter the no:'))

a,b=0,1

if n<=0:
    print('Enter +ve no!')
elif n==1:
    print('Fibonacci sequence up to',n,'terms')
    print(a)
else:
    for i in range(n):
        print(a,end=' ')
        a=b
        b=a+b
    
