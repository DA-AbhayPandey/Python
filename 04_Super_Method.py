# Super method helps in running parent, grandfather or both function at a same time

class grandfather:

  def living(self):
    print("I live in Bharat")

  def jobStatus(self):
    print("I worked in TATA Steel")

  def States(self):
    print("I from Uttar Praddesh")

class father(grandfather):

  def jobStatus(self):
    super().jobStatus()
    print("I worked in Hotel line")

  def States(self):
    print("I from Delhi")

class Employee(father):

  def jobStatus(self):
    super().jobStatus()     #if parent used same super() then it also print the grandfather job status
    print("I work in CISCO")

  def States(self):
    super().States()      #super only prints parents status
    print("I from Mumbai")

g = grandfather()
f = father()
e = Employee()

e.jobStatus()
e.States()

  
