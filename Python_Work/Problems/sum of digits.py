# sum of digites in number

n=int(input("Enter the Number: "))

sum_of_digit=0

while(n>0):
    digit=(n%10)    #to get the last digit of input

    sum_of_digit+=digit     #adding the ' digit ' to sum_of_digit

    n=n//10         # Remove the last digit from 'n'

print("The sum of given Digit is:",sum_of_digit)































