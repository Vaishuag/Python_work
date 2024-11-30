# sum of +ve number and -ve number

count=int(input("Enter the number of value:"))

pos_sum=0
neg_sum=0

i=0
while i<count:
    n=int(input("Enter the number: "))
    if (n>0):
        pos_sum+=n
    elif(n<0):
        neg_sum+=n
    i+=1
print("The sum of Positive number is: ",pos_sum)
print("The sum of Negative number is: ",neg_sum)

        
        
