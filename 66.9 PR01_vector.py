class vector2d:
  def __init__(self, i, j):
    self.icap = i
    self.jcap = j
  
  def __str__(self):
    return f"{self.icap}i + {self.jcap}j"
  
class vector3d(vector2d):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.kcap = k

  def __str__(self):
    return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
  
v2d = vector2d(5, 7)
v3d = vector3d(3, 9, 13)

print(v2d)
print(v3d)
