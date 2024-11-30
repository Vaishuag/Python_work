#Triangle Type Checker

a= float(input("Enter the value of first side:"))
b= float(input("Enter the value of second side:"))
c= float(input("Enter the value of third side:"))

if (a+b>c) and (a+c>b) and (b+c>a):

    if (a==b) and (a==c) and (b==c):
        print(" It's a Equilateral Triangle")
    elif (a==b) or (a==c) or (b==c):
        print("It's a Isosceles Triangle")
    elif (a!=b) and (a!=c) and (b!=c):
        print("It's a Scalen Triangle")
else:
    print("The given lengths do not form a valid triangle")