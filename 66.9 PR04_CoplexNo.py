#Add complex No.(a+bi) + (c+di) = (a+c) + (b+d)i
class Complex:
  def __init__(self, r, i):
    self.real = r
    self.imaginary = i

  def __add__(self, c):
    return f"({self.real + c.real} + {self.imaginary + c.imaginary}i)"
  
  def __mul__(self, c):
    return f"({self.real*c.real - self.imaginary*c.imaginary} + {self.real*c.imaginary + self.imaginary*c.real}i)"
  

  
#Multiply complex No. - (a+bi)(c+di) = (ac−bd) + (ad+bc)i

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1+c2)
print(c1*c2)
