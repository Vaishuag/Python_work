#iterate

l=[1,2,3,4,5]
i=iter(l)

print(next(i))
print(next(i))



#generator
def names():
    n=['ram','sita','ali']
    i=0
    while True:
        x=n[i]
        i=(i+1)%3
        yield x  # yield holds the x value

d=names()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))


#Decorator [to modifey the function without effecting the main function]
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a, b)
    return inner

div=smart_div(div)
div(2,7)


a=10

def some():
    global a
    a=9
    print('inside',a)

some()
print('outside',a)



a,d,c,d=10,20,30,40

def func1(a=10, b=20):
    x,y,z=1,2,3
    print(locals()['x'])

func1()
print(globals()['a'])






