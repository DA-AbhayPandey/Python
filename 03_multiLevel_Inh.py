# MultiLevel Inhetritance works like grandparents to parents to child 

class grandfather:
  country = "Bharat"
  state = "Uttar Pradesh"
  company = "TATA"

  def living(self):
    print("I live in Bharat")

  def jobStatus(self):
    print("I worked in Hotel line")

  def States(self):
    print("I from Uttar Praddesh")

class father(grandfather):
  state = "Delhi"
  company = "ITC Hotel"

  def jobStatus(self):
    print("I worked in Hotel line")

  def States(self):
    print("I from Delhi")

class Employee(father):
  company = "Cisco"

  def jobStatus(self):
    print("I work in CISCO")

g = grandfather()
f = father()
e = Employee()

e.jobStatus()
e.States()
e.living()
print(e.company)
print(e.state)
print(e.country)
  
