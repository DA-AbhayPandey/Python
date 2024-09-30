# Single Inheritance

class Employee:
  company = "Google"

  def showDetails(self):
    print("This is employee of Google")

class Position(Employee):
  role = "Programmer"
  company = "YouTube"

  def jobDescripition(self):
    print(f"Employee is {self.role} at {self.company}")

e = Employee()
p = Position()

e.showDetails()
p.showDetails()

p.jobDescripition()
print(p.company)

#this is the Example of Single Inheritance 
#In single Inheritance , there is only one parent class from which they pick things

