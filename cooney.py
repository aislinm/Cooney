print("Cooney likes summer but he doesn\'t like winter.")
print("Cooney likes soccer but he doesn\'t like hockey.")
print("Cooney likes the moon but he doesn\'t like the sun.")

intGuessCount = 0
intCounter = 0
intGuessSize = 0
blnCooneyAchieved = False
strGuess = "hello"

while strGuess != "":
  if intGuessCount >=5:
    break
  strGuess = input("What does Cooney like?")
  if strGuess =="":
    print("Please enter a guess.")
  else:
    intGuessSize = len(strGuess)
    for i in range(intGuessSize - 1):
      if strGuess[i]==strGuess[i+1]:
        blnCooneyAchieved = True
        break
    else:
      blnCooneyAchieved = False
  if blnCooneyAchieved == False:
    print("Cooney doesn\'t like " + strGuess)
  elif blnCooneyAchieved == True:
    print("Cooney likes " + strGuess)
    blnCooneyAchieved = False
    intGuessCount = intGuessCount + 1

print("No more guesses left.")
