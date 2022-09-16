class Complex:

    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b>0: return f"{self.a}+{self.b}i"
        else: return f"{self.a}{self.b}i"

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __sub__(self,other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a, b)

    def __mul__(self,other):
        a = self.a*other.a - self.b*other.b
        b = self.a*other.b + self.b*other.a
        return Complex (a,b)

    def __truediv__(self,other):
        a = (self.a*other.a + self.b*other.b)/( other.a**2 + other.b**2)
        b = (self.b*other.a - self.a*other.b)/( other.a**2 + other.b**2)
        return Complex (a,b)
    
    def __eq__(self,other):
        return (self.a == other.a) & (self.b == other.b)


