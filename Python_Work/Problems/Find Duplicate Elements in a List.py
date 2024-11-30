# Find Duplicate Elements in a List

list=[1,2,3,4,9,5,6,2,7,6,1,9]

seen=set()
duplicate=set()

for num in list:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)
print('The Duplicate in list are:',duplicate)
