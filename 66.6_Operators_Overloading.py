class Number:
  def __init__(self, num):
    self.num = num
  
  def __add__(self, num2):
    print("Adding Numbers has been completed")
    return self.num+ num2.num
  
  def __sub__(self, num2):
    print("Adding Numbers has been completed")
    return num2.num - self.num
  
n1 = Number(6)
n2 = Number(7)
sum = n1+n2
sub = n2-n1
print(sum)
print(sub)

