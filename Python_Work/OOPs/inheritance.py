class Rectangle:
    def __init__(self,l,b):            # super refer all the thing in parent class
        self.l=l
        self.b=b
    
    def area(self):
        return self.l*self.b
    
class cuboid(Rectangle):

    def __init__(self, l, b, h):
        self.h=h
        super().__init__(l, b) 

    def volume(self):
        return self.l*self.b*self.h
    
c=cuboid(10,34,67)
r=Rectangle(10,23)
print(c.volume())
print(r.area())
print(c.area())

