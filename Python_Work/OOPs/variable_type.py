class Rectangle:
    count=0                                #static var/ class var
    def __init__(self, len, bre):           #instance method
        self.len=len
        self.bre=bre
        Rectangle.count +=1                #class variable

    def getlen(self):                       #accessor
        return self.len

    def setlen(self, l):
        self.len=l

    def area(self):
        return self.len * self.bre 

    def perimeter(self):
        return 2*(self.len+self.bre)
    
    @classmethod
    def countRec(cls):                          #class method
        return cls.count
    
    @staticmethod
    def issquare(len,bre):              # this will not have any self
        return len==bre
    
r1=Rectangle(10,20)
r2=Rectangle(64,23)
print(r1.getlen())
r1.setlen(12)
print(r1.getlen())

print(r1.issquare(10,1))
# print(r1.area())

# print(r1.countRec())
# print(Rectangle.countRec())










# class Test:
#     def __init__(self):
#         self.a=12

#     def fun(self):
#         self.b=34

# t1=Test()
# t1.fun()
# t1.c=25
# print(dir(t1))