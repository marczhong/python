import random

ranum = random.randint(1, 100)



while True:
   guessnum = int(input("Guess a number"))
   
   if guessnum > ranum:
      print("too high")

   elif guessnum < ranum:
      print("too low")

   else:
      print("win")
      break

print("the random num is: ", ranum)


