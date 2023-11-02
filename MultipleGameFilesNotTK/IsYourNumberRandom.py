from random import randint as r


def IsYourNumberRandom():
  Z = r(1, 50)
  A = 0
  X = int(input("Enter a random number between 1 and 50 "))
  seeGuesses = input("Do you want to see the computer's guesses? ")
  if X > 50 or X < 1:
    print("Try again")
    X = int(input("Enter a random number between 1 and 50 "))
  while X != Z:
    if seeGuesses.lower() == "yes" or seeGuesses.lower() == "y":
      print(Z)
    Z = r(1, 50)
    A = A + 1
    if X == Z:
      print("It took the computer", A, "tries to guess your number")