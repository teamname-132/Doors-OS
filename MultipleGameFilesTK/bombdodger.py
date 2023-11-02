import random
import tkinter
from linecache import getline
from tkinter import *
from tkinter import messagebox
from english_words import english_words_lower_alpha_set
from random import choice

def start_bombdodger(user):
  global gameOver
  gameOver = False
  global score
  score = 0
  global highscore
  highscore = score
  global Xscore
  Xanscore = getline(r"MultipleGameFilesTK/bombdodgerPoints.txt", 1)
  Xscore = int(Xanscore)
  global Dscore
  Danscore = getline(r"MultipleGameFilesTK/bombdodgerPoints.txt", 2)
  Dscore = int(Danscore)
  global squaresToClear
  squaresToClear = 0
  play_bombdodger(user)


def play_bombdodger(user):
  create_bombfield(bombfield)
  global score
  if user == "laq 6":
    print("Answers:")
    printfield(bombfield)
  global username
  username = user
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
      global username
      global Xscore
      global Dscore
      if username == "daniel":
        if Dscore <= highscore:
          Dscore = highscore
          with open('MultipleGameFilesTK/bombdodgerPoints.txt', 'r') as file:
            data = file.readlines()
          data[1] = str(Dscore) + '\n'
          with open('MultipleGameFilesTK/bombdodgerPoints.txt', 'w') as file:
            file.writelines(data)
      elif username == "xander":
        if Xscore <= highscore:
          Xscore = highscore
          with open('MultipleGameFilesTK/bombdodgerPoints.txt', 'r') as file:
            data = file.readlines()
          data[0] = str(Xscore) + '\n'
          with open('MultipleGameFilesTK/bombdodgerPoints.txt', 'w') as file:
            file.writelines(data)
      if username == "daniel":
        if Dscore >= highscore:
          highscore = Dscore
      elif username == "xander":
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
        play_bombdodger(username)
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
