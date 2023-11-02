def Gess_my_number():
  number = random.randint(1, 20)
  guess = int(input("i'm thinking of a nummberfrom 1,20. what is it"))
  while guess != number:
    if guess < number:
      print("your nummber is too low")
    else:
      print("your number is to high")
    guess = int(input("pleas try again"))
  print(" you did it")
  exit()