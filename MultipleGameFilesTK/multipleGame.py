import random
import tkinter
from linecache import getline
from tkinter import *
from tkinter import messagebox
from english_words import english_words_lower_alpha_set
from random import choice

def start_bombdodger():
  global gameOver
  gameOver = False
  global score
  score = 0
  global highscore
  highscore = score
  global Xscore
  Xanscore = getline(r"bombdodgerPoints.txt", 1)
  Xscore = int(Xanscore)
  global Dscore
  Danscore = getline(r"bombdodgerPoints.txt", 2)
  Dscore = int(Danscore)
  global squaresToClear
  squaresToClear = 0
  play_bombdodger()


def play_bombdodger():
  create_bombfield(bombfield)
  global score
  global user
  if user == "laq 6":
    print("Answers:")
    printfield(bombfield)
  global window
  window = tkinter.Tk()
  window.title("Bombdodger")
  layout_window(window)
  window.mainloop()


bombfield = []
def create_bombfield(bombfield):
  global squaresToClear
  for row in range(0, 10):
    rowList = []
    for calumn in range(0, 10):
      if random.randint(1, 100) < 20:
        rowList.append(1)
      else:
        rowList.append(0)
        squaresToClear = squaresToClear + 1
    bombfield.append(rowList)


def printfield(bombfield):
  for rowList in bombfield:
    print(rowList)
def layout_window(window):
  for rowNumber, rowList in enumerate(bombfield):
    for columnNumber, columnEntry in enumerate(rowList):
      if random.randint(1, 100) < 25:
        square = tkinter.Label(window, text="    ", bg="darkgreen")
      elif random.randint(1, 100) > 75:
        square = tkinter.Label(window, text="    ", bg="seagreen")
      else:
        square = tkinter.Label(window, text="    ", bg="green")
      square.grid(row=rowNumber, column=columnNumber)
      square.bind("<Button-1>", on_click)


def on_click(event):
  global score
  global highscore
  global gameOver
  global squaresToClear
  global bombfield
  global window
  square = event.widget
  row = int(square.grid_info()["row"])
  column = (square.grid_info()["column"])
  currentText = square.cget("text")
  if gameOver == False:
    if bombfield[row][column] == 1:
      gameOver = False
      square.config(bg="red")
      if score > highscore:
        highscore = score
      else:
        highscore = highscore
      global user
      global Xscore
      global Dscore
      if user == "daniel":
        if Dscore <= highscore:
          Dscore = highscore
          with open('bombdodgerPoints.txt', 'r') as file:
            data = file.readlines()
          data[1] = str(Dscore) + '\n'
          with open('bombdodgerPoints.txt', 'w') as file:
            file.writelines(data)
      elif user == "xander":
        if Xscore <= highscore:
          Xscore = highscore
          with open('bombdodgerPoints.txt', 'r') as file:
            data = file.readlines()
          data[0] = str(Xscore) + '\n'
          with open('bombdodgerPoints.txt', 'w') as file:
            file.writelines(data)
      if user == "daniel":
        if Dscore >= highscore:
          highscore = Dscore
      elif user == "xander":
        if Xscore >= highscore:
          highscore = Xscore
      info = "Game over, your score was " + str(
        score) + " and your highscore is " + str(
          highscore) + ". Do you want to play again?"
      playAgain = messagebox.askyesno(message=info)
      if playAgain == True:
        window.destroy()
        score = 0
        gameOver == False
        bombfield = []
        play_bombdodger()
      else:
        exit()

      #score = 0
      #global username
      #if username == "daniel@bombgame.com":
      #global Dscore
      #Dscore = score
      #elif username == "xander@bombgame.com":
      #global Xscore
      #Xscore = score

      #print(
      #"------------------------------------------Restart-----------------------------"
      #)
      #gameOver == False
      #bombfield = []
      #global window
      #window.destroy
      #play_bombdodger()

    elif currentText == "    ":
      square.config(bg="brown")
      totalbombs = 0
      if row < 9:
        if bombfield[row + 1][column] == 1:
          totalbombs = totalbombs + 1
      if row > 0:
        if bombfield[row - 1][column] == 1:
          totalbombs = totalbombs + 1
      if column > 0:
        if bombfield[row][column - 1] == 1:
          totalbombs = totalbombs + 1
      if column < 9:
        if bombfield[row][column + 1] == 1:
          totalbombs = totalbombs + 1
      if row > 0 and column > 0:
        if bombfield[row - 1][column - 1] == 1:
          totalbombs = totalbombs + 1
      if row < 9 and column > 0:
        if bombfield[row + 1][column - 1] == 1:
          totalbombs = totalbombs + 1
      if row > 0 and column < 9:
        if bombfield[row - 1][column + 1] == 1:
          totalbombs = totalbombs + 1
      if row < 9 and column < 9:
        if bombfield[row + 1][column + 1] == 1:
          totalbombs = totalbombs + 1
      square.config(text=" " + str(totalbombs) + " ")
      squaresToClear = squaresToClear - 1
      score = score + 1
      if squaresToClear == 0:
        gameOver = True
        print("Well done! you found all the safe squares")
        print("Your scor was:", score)
        print(
          " -----------------------------------------Restart----------------------------------"
        )





def encrypt():
  global encrypterRoot
  global stringtoencrypt
  global stringtoencryptInput
  global shiftamountstrInput
  alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
  stringtoencrypt = stringtoencryptInput.get()
  shiftamountstr = shiftamountstrInput.get()
  stringtoencrypt = stringtoencrypt.upper()
  try:
    shiftamount = int(shiftamountstr)
  except:
    print("a whole number.")
    exit()
  encrypyrdstring = ""
  for currentcharacter in stringtoencrypt:
    position = alphabet.find(currentcharacter)
    newposition = position + shiftamount
    if currentcharacter in alphabet:
      encrypyrdstring = encrypyrdstring + alphabet[newposition]
    else:
      encrypyrdstring = encrypyrdstring + alphabet[newposition]
  string = " Your message is " + str(stringtoencrypt) + "\n Your encrypted message is " + str(encrypyrdstring)
  Labela = Label(encrypterRoot,text=string)
  Labela.grid(row=3,column=0)
def code_incripter():
  global stringtoencrypt
  global shiftamountstr
  global stringtoencryptInput
  global shiftamountstrInput
  global encrypterRoot
  encrypterRoot = Tk()
  encrypterRoot.title("Encrypter")
  stringtoencryptLabel = Label(encrypterRoot,text="Please enter a message to encrypt:")
  stringtoencryptLabel.grid(column=0,row=0,columnspan=2)
  stringtoencryptInput = Entry(encrypterRoot)
  stringtoencryptInput.grid(column=2,row=0)
  shiftamountstrLabel = Label(encrypterRoot,text="To encrypt, enter a whole number from 1-25 to be your key.\n To decrypt, do that number but minus")
  shiftamountstrLabel.grid(column=0,row=1,columnspan=2)
  shiftamountstrInput = Entry(encrypterRoot)
  shiftamountstrInput.grid(column=2,row=1)
  submitButton = Button(encrypterRoot,text="Submit",command=encrypt)
  submitButton.grid(column=0,row=2)




def aliens_guess():
  global entry1
  global aliens
  global password
  guess = entry1.get()
  if guess != password:
    aliens = aliens**2
    string = "Incorrect password. " + "There are " + str(
      aliens) + " aliens now on Earth. Try again!"
    tkinter.messagebox.showinfo(title="info", message=string)
    tkinter.messagebox.showinfo(
      title="password hint",
      message="Password hint: 'the things that are attacking us'.")
    if aliens > 7400000000:
      tkinter.messagebox.showinfo(
        title="no!",
        message="Nooooooooo! the aliens out numbered us, all is lost!")
      exit()
  else:
    tkinter.messagebox.showinfo(title="Victory!",
                                message="Hooray! We won the world is saved!")
    again = tkinter.messagebox.askyesno(title="",
                                        message="Do you want to play again?")
    if again == True:
      global aliensRoot
      aliensRoot.destroy()
      alions()
    else:
      exit()


def alions():
  global password
  password = "aliens"
  global aliens
  aliens = 2
  global aliensRoot
  aliensRoot = Tk()
  aliensRoot.title("Aliens")
  label1 = Label(aliensRoot, text="Quickly! Aliens are invading the planet.")
  label2 = Label(aliensRoot, text="You need to activate the global platforms.")
  label3 = Label(aliensRoot,
                 text="Hope you know the password, for Earth's sake.")
  labelSpace = Label(aliensRoot, text="")
  label1.grid(column=0, row=0, columnspan=3)
  label2.grid(column=0, row=1, columnspan=3)
  label3.grid(column=0, row=2, columnspan=3)
  labelSpace.grid(column=0, row=3)
  label4 = Label(
    aliensRoot,
    text="---------------------------------------------------------")
  label4.grid(column=0, row=4, columnspan=3)
  label5 = Label(
    aliensRoot,
    text="       Welcome to the global defence network             ")
  label5.grid(column=0, row=5, columnspan=3)
  label6 = Label(
    aliensRoot,
    text="---------------------------------------------------------")
  label6.grid(column=0, row=6, columnspan=3)
  labelSpace2 = Label(aliensRoot, text="")
  labelSpace2.grid(column=0, row=7)
  label7 = Label(aliensRoot, text="Please enter the password: ")
  label7.grid(column=0, row=8)
  global entry1
  entry1 = Entry(aliensRoot)
  entry1.grid(row=8, column=1)
  button1 = Button(aliensRoot, text="Submit password", command=aliens_guess)
  button1.grid(column=0, row=9, columnspan=2)






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


def random_story_cube():
  woman = ["A scientist", "a queen", "a pirate", "a giant rabbit"]
  man = ["a police officer", "an artist", "Your grandfather", "a killer robot"]
  place = ["on Pluto ", "at the supermarket", "in a spooky, bat-filled cave"]
  shewore = ["scuba diving gear", "fairy wings", "paper bag"]
  hewore = ["a purple suit", "a shark costume", "beach towel"]
  womansays = [
    "let’s go to the beach", "let’s go to the moon", "let’s go to spain"
  ]
  mansays = ["ok", "no let’s go cycling", "yes let’s go"]
  consequence = [
    "there got squashed by a giant frog", "got lost", "met a creepy horse"
  ]
  worldsaid = [
    "run over by a car", "fell into a dich", " lost all of their money"
  ]
  while True:
    print(random.choice(woman), "met", random.choice(man),
          random.choice(place))
    print("she was wearing", random.choice(shewore))
    print("he was wearing", random.choice(hewore))
    print("she said", random.choice(womansays))
    print("he said", random.choice(mansays))
    print("On their travels", random.choice(consequence), "and",
          random.choice(worldsaid))
    print()
    print(
      "--------------------------------------------------------------------")
    print()
    hi = input("press enter to play again or to not type stop ").upper()
    if hi == "STOP":
      exit()
    print()
    print(
      "--------------------------------------------------------------------")
    print()


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


def bat_ball_game():
  import turtle
  from turtle import listen
  import os
  global wn
  global ball
  global paddle_a
  global paddle_b
  global score_a
  global score_b
  global pen
  wn = turtle.Screen()
  wn.title("Pong Game By Multiple Game Devs")
  wn.bgcolor("black")
  wn.setup(width=800, height=600)
  wn.tracer(0)
  score_a = 0
  score_b = 0
  paddle_a = turtle.Turtle()
  paddle_a.speed(0)
  paddle_a.shape("square")
  paddle_a.color("red")
  paddle_a.shapesize(stretch_wid=5, stretch_len=1)
  paddle_a.penup()
  paddle_a.goto(-350, 0)
  paddle_b = turtle.Turtle()
  paddle_b.speed(0)
  paddle_b.shape("square")
  paddle_b.color("green")
  paddle_b.shapesize(stretch_wid=5, stretch_len=1)
  paddle_b.penup()
  paddle_b.goto(350, 0)
  ball = turtle.Turtle()
  ball.speed(0)
  ball.shape("circle")
  ball.color("yellow")
  ball.penup()
  ball.goto(0, 0)
  ball.dx = 0.1
  ball.dy = 0.1
  pen = turtle.Turtle()
  pen.speed(0)
  pen.shape("square")
  pen.color("white")
  pen.penup()
  pen.hideturtle()
  pen.goto(0, 260)
  pen.write("Player A: 0 Player B: 0",
            align="center",
            font=("Courier", 24, "normal"))


def paddle_a_up():
  global paddle_a
  global paddle_b
  global wn
  global ball
  global score_a
  global pen
  global score_b
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)


def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)


def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)


def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

def start_bat():
  bat_ball_game()
  global wn
  global ball
  global paddle_a
  global paddle_b
  global score_a
  global score_b
  global pen
  wn.listen()
  wn.onkeypress(paddle_a_up, "a")
  wn.onkeypress(paddle_a_down, "z")
  wn.onkeypress(paddle_b_up, "Up")
  wn.onkeypress(paddle_b_down, "Down")
  while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
    elif ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
    if ball.xcor() > 350:
      score_a += 1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                align="center",
                font=("Courier", 24, "normal"))
      ball.goto(0, 0)
      ball.dx *= -1
    elif ball.xcor() < -350:
      score_b += 1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                align="center",
                font=("Courier", 24, "normal"))
      ball.goto(0, 0)
      ball.dx *= -1
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor(
    ) > paddle_a.ycor() - 50:
      ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor(
    ) > paddle_b.ycor() - 50:
      ball.dx *= -1

import tkinter as TK
import time
def bouncy_ball():
  global  VERT,HOREZ,xTOP,yTOP,xBTM,yBTM,MAX_WIDTH,MAX_HEIGHT,xSTART,ySTART,BALL_SIZE,RUNNING
  VERT,HOREZ=0,1
  xTOP,yTOP = 0,1
  xBTM,yBTM = 2,3
  MAX_WIDTH,MAX_HEIGHT = 640,480
  xSTART,ySTART = 100,200
  BALL_SIZE=20
  RUNNING=True
  start_bounce()
def close():
  global RUNNING
  RUNNING=False
  root.destroy()

def move_right(event):
  if canv.coords(paddle)[xBTM]<(MAX_WIDTH-7):
    canv.move(paddle, 7, 0)

def move_left(event):
  if canv.coords(paddle)[xTOP]>7:
    canv.move(paddle, -7, 0)

def determineDir(ball,obj):
  global delta_x,delta_y
  if (ball[xTOP] == obj[xBTM]) or (ball[xBTM] == 
      obj[xTOP]):
    delta_x = -delta_x
  elif (ball[yTOP] == obj[yBTM]) or (ball[yBTM] == 
        obj[yTOP]):
    delta_y = -delta_y
def start_bounce():
  global  VERT,HOREZ,xTOP,yTOP,xBTM,yBTM,MAX_WIDTH,MAX_HEIGHT,xSTART,ySTART,BALL_SIZE,RUNNING
  global root,canv,top,left,right,bottom,ball,paddle,delta_y,delta_x
  root = TK.Tk()
  root.title("Bouncing Ball By Multiple Game")
  root.geometry('%sx%s+%s+%s' %(MAX_WIDTH, MAX_HEIGHT, 100, 100))
  root.bind('<Right>', move_right)
  root.bind('<Left>', move_left)
  root.protocol('WM_DELETE_WINDOW', close)
  canv = TK.Canvas(root, highlightthickness=0)
  canv.pack(fill='both', expand=True)
  top = canv.create_line(0, 0, MAX_WIDTH, 0, fill='blue',tags=('top'))
  left = canv.create_line(0, 0, 0, MAX_HEIGHT, fill='blue',tags=('left'))
  right = canv.create_line(MAX_WIDTH, 0, MAX_WIDTH, MAX_HEIGHT,fill='blue', tags=('right'))
  bottom = canv.create_line(0, MAX_HEIGHT, MAX_WIDTH, MAX_HEIGHT,fill='blue', tags=('bottom'))
  ball = canv.create_rectangle(0, 0, BALL_SIZE, BALL_SIZE,outline='black', fill='green', tags=('ball'))
  paddle = canv.create_rectangle(100, MAX_HEIGHT - 30, 150, 470,outline='black', fill='red', tags=('rect'))
  brick=list()
  for i in range(0,16):
    for row in range(0,4):
      brick.append(canv.create_rectangle(i*40, row*20,
                   ((i+1)*40)-2, ((row+1)*20)-2,
                   outline='black', fill='blue',
                   tags=('rect')))
  
  delta_x = delta_y = 1
  xold,yold = xSTART,ySTART
  canv.move(ball, xold, yold)
  while RUNNING:
    objects = canv.find_overlapping(canv.coords(ball)[0],
                                    canv.coords(ball)[1],
                                    canv.coords(ball)[2],
                                    canv.coords(ball)[3])
  
    dir_changed=False
    for obj in objects:
      if (obj != ball):
        if dir_changed==False:
          determineDir(canv.coords(ball),canv.coords(obj))
          dir_changed=True
        if (obj >= brick[0]) and (obj <= brick[len(brick)-1]):
          canv.delete(obj)
        if (obj == bottom):
          text = canv.create_text(300,100,text="YOU MISSED!")
          canv.coords(ball, (xSTART,ySTART,
                      xSTART+BALL_SIZE,ySTART+BALL_SIZE))
          delta_x = delta_y = 1
          canv.update()
          time.sleep(3)
          canv.delete(text)
    new_x, new_y = delta_x, delta_y
    canv.move(ball, new_x, new_y)
  
    canv.update()
    time.sleep(0.0095)
  brick=list()
  for i in range(0,16):
    for row in range(0,4):
      brick.append(canv.create_rectangle(i*40, row*20, 
                   ((i+1)*40)-2, ((row+1)*20)-2, outline='black', 
                   fill='red', tags=('rect')))
  if (ball[xTOP] == obj[xBTM]) or (ball[xBTM] == obj[xTOP]):
      delta_x = -delta_x
  brick=list()
  for i in range(0,16):
    for row in range(0,4):
      brick.append(canv.create_rectangle(i*40, row*20, 
                   ((i+1)*40)-2, ((row+1)*20)-2, outline='black', 
                   fill='red', tags=('rect')))


def startCalc():
    global calculatorRoot
    global e
    calculatorRoot = Tk()
    calculatorRoot.title("Simple Calculator By Multiple Game")
    e = Entry(calculatorRoot, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3)
    calcButtons()
f_num = 0
def button_click(number):
    global e
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonclear():
    global e
    e.delete(0, END)
def buttonequals():
    global e
    second_number = e.get()
    e.delete(0, END)
    if second_number == "":
        second_number = 0
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math == "division":
        e.insert(0, f_num / float(second_number))

def buttonadd():
    global e
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def buttonsubtract():
    global e
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)
    
def buttonmultiply():
    global e
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def buttondivide():
    global e
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)
def calcButtons():
    global calculatorRoot
    button_1 = Button(calculatorRoot, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(calculatorRoot, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(calculatorRoot, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(calculatorRoot, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(calculatorRoot, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(calculatorRoot, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(calculatorRoot, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(calculatorRoot, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(calculatorRoot, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(calculatorRoot, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_add = Button(calculatorRoot, text="+", padx=39, pady=20, command=buttonadd)
    button_equals = Button(calculatorRoot, text="=", padx=88, pady=20, command=buttonequals)
    button_clear = Button(calculatorRoot, text="Clear", padx=78, pady=20, command=buttonclear)
    button_subtract = Button(calculatorRoot, text="-", padx=41, pady=20, command=buttonsubtract)
    button_multiply = Button(calculatorRoot, text="X", padx=39, pady=20, command=buttonmultiply)
    button_divide = Button(calculatorRoot, text="÷", padx=39, pady=20, command=buttondivide)
    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)
    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)
    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)
    button_0.grid(row=4,column=0)
    button_clear.grid(row=4,column=1, columnspan=2)
    button_add.grid(row=5,column=0)
    button_equals.grid(row=5,column=1, columnspan=2)
    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    calculatorRoot.mainloop()

from english_words import english_words_lower_alpha_set
from random import choice


def hangman():
  play = "yes"
  while play != "no":
    howManyGuesses = 0
    word = choice(list(english_words_lower_alpha_set))
    letters = []
    board = []
    for x in word:
      letters+= [x]
      board+= [""]
    guesses = []
    while guesses[0:] != letters[0:]:
      guess = input("Guess: ").lower()
      if guess == "":
        print("Not a letter.")
      elif len(guess) > 1:
        print("One letter")
      elif guess in guesses and letters.count(guess) == guesses.count(guess):
        print("Already guessed.")
      elif guess not in letters:
        print("No")
        howManyGuesses+=1
      elif guess in letters and letters.count(guess) > 1:
        print("Yes")
        howManyGuesses+=1
        print("There were",letters.count(guess),"of the letter",guess,"in the word")
        counted = letters.count(guess)
        a = counted
        pos = -1
        while a != 0:
          guesses += [guess]
          index = letters.index(guess, pos+1, len(letters))
          pos = index
          board[index] = guess
          a-=1
        print("Board:",('_'.join(board)))
      else:
        howManyGuesses+=1
        print("Yes")
        guesses += [guess]
        index = letters.index(guess)
        board[index] = guess
        print("Board:",('_'.join(board)))
      if sorted(guesses[0:]) == sorted(letters[0:]):
        print("You got that in",howManyGuesses,"guesses.")
        print("Well done!")
        play = input("Do you want to play again? Press enter to continue and no to stop. ")

def gamesSubmitCommand():
  global gamesInput
  global Gamesroot
  gameChoice = gamesInput.get()
  Gamesroot.destroy()
  if gameChoice == "bombdodger":
    start_bombdodger()
  elif gameChoice == "tic tac toe":
    print("tic tac toe")
    TicTacToe()
  elif gameChoice == "guess my number":
    Gess_my_number()
  elif gameChoice == "times tables":
    Times_mashen()
  elif gameChoice == "story":
    print()
    random_story_cube()
  elif gameChoice == "encrypter":
    pasword3 = input("password")
    if pasword3 == "C0DE":
      code_incripter()
    else:
      print("Stop tring to hack us")
      exit()
  elif gameChoice == "aliens":
    print()
    alions()
  elif gameChoice == "is your number random":
    IsYourNumberRandom()
  elif gameChoice == "bat and ball":
    start_bat()
  elif gameChoice == "calculator":
    startCalc()
  elif gameChoice == "bouncy ball":
    bouncy_ball()
  elif gameChoice == "hangman":
    hangman()
  else:
    print("We do not have that game")
    selectGame()


def selectGame():
  games = [
    "Bombdodger", "Encrypter", " Aliens", "Calculator", "Times tables",
    "Guess my number", "Tic Tac Toe\n", "Story", "Is Your Number Random", "TK Bat and ball","TK basy ball", "hangman"
  ]
  #Bombdodger, Aliens and Calculator completed
  gamesLength = len(games)
  gamesString = "Games: " + ', '.join(
    games[0:gamesLength - 1]) + " or " + games[gamesLength - 1]
  global Gamesroot
  Gamesroot = Tk()
  Gamesroot.title("Pick a game")
  gamesLabel = Label(Gamesroot, text=gamesString)
  gamesLabel.grid(row=0, column=0, columnspan=300)
  global gamesInput
  gamesInput = Entry(Gamesroot)
  gamesInput.grid(row=1, column=0)
  gamesSubmit = Button(Gamesroot, text="submit", command=gamesSubmitCommand)
  gamesSubmit.grid(row=2, column=0)


a = 1
infoFound = False


from linecache import getline
from tkinter import Label,Entry,Tk,Button
import json
import bcrypt

with open ("users.json", "r") as file:
  users = json.loads(file.read())

def signUp():
  global hoorayLabel
  hoorayLabel.config(text="We have signed you up because you \n didn't have an account")

root = Tk()

nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=0, column=0)

nameInput = Entry(root)
nameInput.grid(row=0, column=1)

passLabel = Label(root, text="Password: ")
passLabel.grid(row=1, column=0)

passInput = Entry(root)
passInput.grid(row=1,column=1)

hoorayLabel = Label(root, text="Waiting on input...")
hoorayLabel.grid(row=4,column=0,columnspan=2)

def submit():
  global users
  global root
  global hoorayLabel
  global user
  isnew = False
  username = nameInput.get().lower()
  password = passInput.get()
  try:
    user = users[username]
  except:
    print("Creating account...")
    isnew = True
    user = {"password":bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('ascii'),"name":username}
    users[username] = user
    data = json.dumps(users, indent=2)
    with open ("users.json", "w") as file:
      file.write(data)
  if isnew:
    signUp()
  elif bcrypt.checkpw(password.encode('utf-8'),user["password"].encode('utf-8')):
    hoorayLabel.config(text="Signed in")
    root.destroy()
    selectGame()
  else:
    hoorayLabel.config(text="Wrong password.")
submit = Button(root, text="Submit", command=submit)
submit.grid(row=3,column=0)


root.mainloop()
