def Times_mashen():
  editchoice = " Nothing "
  while editchoice != "EXIT":
    table = int(input("please tipe a tible:"))
    number = int(input("Up to"))
    for x in range(0, number + 1):
      print(x, "x", table, "=", x * table)
    editchoice = input(
      "press reatern to play again, or tipe EXIT to leave ").upper()
    if editchoice == "EXIT":
      exit()