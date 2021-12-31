import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def valid(self):
        return ((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a))
    
    def is_valid(self):
        if(self.valid()):
            return 'Valid'
        else:
            return 'Invalid'
    
    
        
    def Side_Classification(self):
        if(not self.valid()):
            return 'Invalid'
        if(self.a == self.b == self.c):
            return 'Equilateral'
        if(self.a == self.b or self.a == self.c or self.b == self.c):
            return 'Isosceles'
        return 'Scalene'
    
    def Angle_Classification(self):
        if(not self.valid()):
            return 'Invalid'
        a2b2 = a*a + b*b 
        c2 = c*c
        if a2b2 > c2:
            return 'Acute'
        if a2b2 == c2:
            return 'Right'
        return 'Obtuse'
    
    def Area(self):
        if(not self.valid()):
            return 'Invalid'
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s- self.a) * (s -self.b) * (s-self.c))
        
a=10
b=3
c=5
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())