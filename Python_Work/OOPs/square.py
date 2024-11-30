import math

class sphere:
    def __init__(self, radious):
        self.radious=radious

    def surface_area(self):
        return 4* math.pi * (self.radious**2)
    
    def volume(self):
        return (4/3)* math.pi* (self.radious**3)
    
s=sphere(8)

print('Surface area of Sphere is :',round(s.surface_area(),2))
print('Volume of sphere is :', round(s.volume(),2))