#Count Elements by Condition

num_list=[2,-8,5,12,9,16,-7]
print(num_list)
count={'positive':0,
       'negitive':0,
       'even':0,
       'odd':0}
for num in num_list:
    if num>0:
        count['positive']+=1 # inital value of +ve is '0'
    else:
        count['negitive']+=1 
        
    if num%2==0:
        count['even']+=1
    else:
        count['odd']+=1
print(count)
        
