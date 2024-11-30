import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def semi_perimeter(self):
        return self.perimeter() / 2

    def area(self):
        s = self.semi_perimeter()
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

triangle = Triangle(3, 4, 5)
print("Perimeter of Triangle:", triangle.perimeter())    
print("Area of Triangle:", round(triangle.area(), 2))    
