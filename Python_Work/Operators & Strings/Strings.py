# STRING
print('ram'"'"'s')
print('ram\'s') #escape character


# concatinate
d1='abc'
d2='def'
print(d1+d2) 
print(d1*3)
print(len(d1*3))
'''
'''
#SLICING
s3='hello world'
len(s3)
print(s3[0:11:1])

#IN
print('o' in s3)
print('me' not in s3)

#dir(S)
#help(s.endswith)
    
# FIND
#syntax: sub(start,end)
s='hello world'
print(len(s))
print(s.find('o'))

print(s.find('o',5))

#rfind : searching from right side
print(s.rfind('o'))     

# INDEX
print(s.find('o'))

# COUNT
print(s.count('l'))


#ljust(width, fillchar=' ',/)
S=input()
print(S.rjust(10))
print(S.center(10))
print(S.ljust(10,'*'))
print(S.rjust(10,'*'))
print(S.center(10,'*'))

#  STRIP()
s4='h    hello world   '
print(s4)
print(s4.strip())
print(s4.strip('.+'))


s5='hello world'
print(s5.capitalize())
print(s5.upper())
print(s5.lower())
print(s5.swapcase())
print(s5.title())
print(s5.isalnum())
print(s5.isalpha())
print(s5.isspace())

# JOIN
s6='123'
s7='abc'
print(s6.join(s7))

# SPLIT [ it take string input, give list value
s8='john smith ajay'
s9='a-b-c-d-e-f-g-h'
print(s8.split('h'))
print(s9.split('-'))










