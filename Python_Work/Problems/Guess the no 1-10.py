# Guess the number b/w 1 to 10

import random
r= random.randint(1,10)
guess=0
while guess!=r:
    guess=int(input("Enter the guess value: "))
    if guess<r:
        print("It's is Smaller value!!")
    elif guess>r:
        print("It's is Bigger value!!")
    else:
        print("Correct Guess!!")
               
