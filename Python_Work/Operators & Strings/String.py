# String
# 1)Concatenate two strings

s1='vaishnavi '
s2='A G'
print(s1+s2)

# 2)Repeat a string multiple times

s='Goal'
print(s*3)

# 3)Slice a string
a='Bangalore'
print(a[0:6:1])
print(a[-1:-8:-2])
print(a[:9:2])


# 4)Check if a character or substring is in the string

b='Mysore'
print('y' in b) #IN
print('nh' in b)

#5)Find and count occurrences of characters/substrings
c='vaishnavi'
print(c.find('s')) 
print(c.find('e',0,3))


#6)Adjust text alignment

d='Welcome'
print(d.ljust(10,'^'))
print(d.rjust(10,'^'))
print(d.center(13,'^'))

# 7) Strip unwanted characters
e=' Good evening '
print(e.strip(' '))

#8)Change text case

f='vaishnavi girish'
print(f.upper())
print(f.lower())
print(f.swapcase())
print(f.title())

#9)Join characters with a delimiter

h='*'
g='abc'
print(h.join(g))

#10)Split the string by a delimiter

i='1*2*3*4*5*6'
print(i.split('*'))

'''s='kamlogb'
h=(sorted(s))
print(''.join(h))
'''






