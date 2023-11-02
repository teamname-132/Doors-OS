def TicTacToe():
  global E
  global X
  global O
  E = " "
  X = "X"
  O = "O"
  global G
  G = [[E, E, E], [E, E, E], [E, E, E]]
  global Turn
  global Won
  global Drew
  #dev = input("Pin: ")
  #if dev == "1234":
  #    print("Simulating if X won...")
  #    whenGameIsWon("X")
  #else:
  #    print("")
  Turn = "X"
  Won = False
  Drew = False
  print(
    "---------------------------------------------------------------------------------------------------------"
  )
  print("                                            Tic-Tac-Toe")
  print(
    "---------------------------------------------------------------------------------------------------------"
  )
  print()
  print("Format for choice: A/B/C 1/2/3 no spaces")
  print()
  PlayTurn()


def whenGameIsWon(winner):
  global PlayAgain
  print("Well done", winner, " for winning!")
  PlayAgain = input("Do you want to play again?")
  if PlayAgain.lower() == "yes" or PlayAgain.lower(
  ) == "yeah" or PlayAgain.lower() == "ye" or PlayAgain.lower() == "y":
    TicTacToe()
  else:
    print("Game stopped")
    exit()


def checkForWinner():
  global Won
  global Drew
  global E
  global X
  global O
  global G
  #X wins if

  for a in range(0, 2):
    if G[0][a] != E and G[0][a] == G[1][a] == G[2][a]:
      Won = True
      whenGameIsWon(G[0][a])
      return ()
    if G[a][0] != E and G[a][0] == G[a][1] == G[a][2]:
      Won = True
      whenGameIsWon(G[a][0])
      return ()
  if G[0][0] != E and G[0][0] == G[1][1] == G[2][2]:
    Won = True
    whenGameIsWon(G[0][0])
    return ()
  if G[2][0] != E and G[2][0] == G[1][1] == G[0][2]:
    Won = True
    whenGameIsWon(G[2][0])
    return ()


def printGameboard():
  global G
  print()
  print(
    "---------------------------------------------------------------------------------------------------------"
  )
  print("Gameboard:")
  print("  1  2  3")
  print("A|", G[0][0], "|", G[0][1], "|", G[0][2])
  print("B|", G[1][0], "|", G[1][1], "|", G[1][2])
  print("C|", G[2][0], "|", G[2][1], "|", G[2][2])
  print(
    "---------------------------------------------------------------------------------------------------------"
  )
  print()


def taketurn(player):
  checkForWinner()
  global G
  global choice
  if len(choice) != 2:
    print("Invalid")
    PlayTurn()
    return ()
  a = "ABC".find(choice[0])
  b = "123".find(choice[1])

  if a < 0 or b < 0:
    print("Invalid")
    PlayTurn()
    return ()
  else:
    G[a][b] = player
  checkForWinner()
  global Turn
  if Turn == X:
    Turn = O
    PlayTurn()
  elif Turn == O:
    Turn = X
    PlayTurn()
  else:
    print("Invalid Turn")
    exit()


def PlayTurn():
  printGameboard()
  global Turn
  print("It is ", Turn, "'s turn")
  global choice
  choice = input("Choice: ")
  print("Choice: ", choice)

  taketurn(Turn)
  printGameboard()