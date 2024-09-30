#Multiple Inheritance is when the child inherits from more than one parents ...

class Employee:
  company = "Wipro"
  Id = 23467

class Freelancer:
  company = "Fever"
  Level = 0

  def upgradeLevel(self):
    self.Level=self.Level+1
    print(f"You level up to Level {self.Level}")

class Details(Employee, Freelancer):
  name = "Abhay"
  position = "Associate"

d = Details()
d.upgradeLevel()
print(d.company)   #child always print the first parent details used in class
                    # for exaample if we create class Details(Freelancer, Employee)
                    #then it print company from class Freelancer 
