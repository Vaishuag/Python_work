import  math

class Cylinder:
    def __init__(self, radius, height):
        self.radius=radius
        self.height=height

    def lateral_area(self):
        return 2* math.pi * self.radius * self.height
    
    def total_area(self):
        return 2* math.pi* self.radius* (self.radius+self.height)
    
    def volume(self):
        return math.pi* (self.radius**2) * self.height

c= Cylinder(6,4)

print("Lateral Area of Cylinder:", round(c.lateral_area(), 2))  
print("Total Surface Area of Cylinder:", round(c.total_area(), 2))  
print("Volume of Cylinder:", round(c.volume(), 2))              
