import random
RandomNumb = random.randint(1,100)
#print(RandomNumb)
UserNumb = None
guesses = 0

while (UserNumb != RandomNumb):
  UserNumb = int(input("Please guess your number:\n"))
  guesses += 1
  if (RandomNumb == UserNumb):
   print("You guess the right number")
  else:
   if (RandomNumb > UserNumb):
    print("Your guess is wrong, Your number is smaller than correct one")
   else:
    print("Your guess is wrong, Your number is bigger than correct one")

print(f"You guess the number in {guesses} attempt")

with open("Highscore.txt","r") as h:
 Highscore = int(h.read())

if (Highscore>guesses):
 print("Congrats you just broke the highscore")
 with open ("Highscore.txt", "w") as h:
  h.write(str(guesses))
