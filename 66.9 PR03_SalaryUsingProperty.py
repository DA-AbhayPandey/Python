class Employee:
  salary = 1000
  increment = 0.2

  @property
  def TotalIncrement(self):
    return self.salary*self.increment
  
  @TotalIncrement.setter
  def TotalIncrement(self, sal):
    self.increment=sal/self.salary

  

e = Employee()
print(e.TotalIncrement)
print(e.increment)
e.TotalIncrement = 500
print(e.TotalIncrement)
print(e.increment)


