# Tuple Operations

#Length and Iteration

print('Length of Tuple')
t3=('abc',2,-7,'546',3)
print(len(t3))


# Tuple Methods

#count()
print('count')
t4=(2,5,7,6,4,7,3,0)
print(t4.count(7))
print(t4.count(2),'\n')

print('index of 6 is:')
print(t4.index(6))


# Check if an element is in a tuple using in and not in

print('Check if an element is in a tuple using in and not in.')
t5=('tab','shift','capsLK',27,4,42)
print(1 in t5)
print('tab' in t5)
print('LK' in t5)
print(t5.index(42))


#Concatenation and Repetition: Combine tuples using + or repeat using *.

print('Concatenation of tuples')
t1=(5,10,15,20)
t2=(25,30,35,40)
t=(111,222,333)
print(t1,'\n',t2)
print(t1+t2,'\n')

print('repetation of tuple')
print(t*2)



# Indexing and Slicing: Access elements by index or get a slice of the tuple.

t6=(1,23,'hello',6,5,'monkey')
print('Tuple Indexing')
print(t6[2],'\n')

print('tuple slicing')
print(t6[1:4])
print(t6[:-5:-1])


