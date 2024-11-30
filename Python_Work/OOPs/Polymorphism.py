# def Driver(car):
#     car.driver()

# class Creta:
    
#     def driver(self):
#         print('creat is driving')           #duck typing

# class Mercedes:
#     def driver(self):
#         print('Mercidies is driving')

# c=Creta()
# m=Mercedes()
# Driver(c)
# Driver(m)




#example for method over loading
# class Arith:
#     def sum(self, x,y, z=None):
#         s=x+y
#         if z==None:
#             return s
#         else:
#             return s+z
    
# a=Arith()
# print(a.sum(10,20))

# print(a.sum(5,10))



#method overriding

# class O_Nokia:
#     def home(self):
#         print('home button is pressed')
    
# class N_Nokia(O_Nokia):
#     def home(self):
#         print('Home is touched')
#         super().home()

# o=O_Nokia()
# o.home()

# n=N_Nokia()
# n.home()


a=3
b=4

print(a+b)
#print(int.__add__(a,b))