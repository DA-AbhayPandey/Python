# Property decorater also know as getter

class Employee:
  salary = 5000
  bonusSalary = 500
  #total salary = 5500  but if we change salary or bonus then total salary still remain 6000

  @property            #propert also know as getter used to set function as property in class
  def TotalSalary(self):
    return self.salary+self.bonusSalary
  
  @TotalSalary.setter   #setter used with property to create new function
  def TotalSalary(self, val):
    self.bonusSalary = val - self.salary
  
e = Employee()
print(e.TotalSalary)
e.TotalSalary = 6000
print(e.salary)
print(e.bonusSalary)
  

