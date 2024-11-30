#variable
x=15    #int
y=7.3    #float
IP=3.14   #Constraints

print("x value=", x)
print("y value=", y)
print("        ")

print("type function")
print("x type =",type(x),"id=",id(x))
print("y type =",type(y),"id=",id(y))
print("        ")

#Boolean value
value_1=x>y
value_2=x==y
print("Boolean Values")
print("15>7.3",value_1)
print("15==7.3",value_2)
print("        ")

#Complex value(a+bj)
s1=3+5j
k1=2+7j
print("Complex value")
print(s1+k1)
print(s1-k1)
print("        ")


#List
skills=["Power BI","Excel","Python","VBA"]
print("List")
print(skills)
skills.append("Tableau")
print("1 value of list is -",skills[1])
print(skills)
skills.insert(1,"AI/ML") #inserting value in a required index

skills.extend(["C","C++"]) #inserting multiple value at once
print(skills)
print("        ")

#Tuples
Courses=("java","C++","Python","C")
print("Tuple")
print(Courses)
print(Courses[2])
print("        ")

a,b=23.5,4
print(a)
print(b)
print("        ")

#Strings
j="Strings"
print("Strings")
print("j[-3]=",j[-3])
print("j[3]=",j[3])
print("        ")


#None
z=None
print(type(z))

s=[[5,6],'abc',(1,2),5]
print(s)
print(s[2])




















