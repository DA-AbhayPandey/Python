import random

def GameResult(Computer, You):
  if Computer==You:
    return None
  elif Computer=='r':
    if You=='p':
      return True
    elif You=='s':
      return False
  elif Computer=='p':
    if You=='s':
      return True
    elif You=='r':
      return False
  elif Computer=='s':
    if You=='r':
      return True
    elif You=='p':
      return False


Computer=("Computer selecting his attack: Rock(r) Paper(p) or Scissor(s)")
compselection=random.randint(1,3)
if compselection ==1:
  Computer='r'
elif compselection ==2:
  Computer='p'
elif compselection==3:
  Computer='s'

You=input("Choose your attack: Rock(r) Paper(p) or Scissor(s)\n")

game=GameResult(Computer, You)

if Computer == 's':
  print("Computer choosed Scissor ")
elif Computer == 'p':
  print("Computer choosed Paper ")
elif Computer == 'r':
  print("Computer choosed Rock ")

if You == 's':
  print("You choosed Scissor ")
elif You == 'p':
  print("You choosed Paper ")
elif You == 'r':
  print("You choosed Rock ")

if game == None:
  print("Game is Tie")
elif game:
  print("You win")
else:
 print("You Loose")
