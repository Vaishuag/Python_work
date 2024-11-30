# multiplication of  given numbers

n=int(input("Enter the Number: "))

multiplication_of_digit=1

while(n>0):
    digit=(n%10)    #to get the last digit of input

    multiplication_of_digit=digit *  multiplication_of_digit    #multiple of ' digit ' with multiplication_of_digit

    n=n//10         # Remove the last digit from 'n'

print("The sum of given Digit is:",multiplication_of_digit)

