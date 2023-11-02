from tkinter import *
import tkinter
from PIL import Image, ImageTk

from MultipleGameFilesTK.bombdodger import *

from WordProscessor.word import start as wordStart


import time as T

#from newfiles.main import start as translatestart

def bombdodge(user):
  start_bombdodger(user)

def word():
  wordStart()

def translate():
  translatestart()

def generate(user):
  global bombPhoto, root, wordPhoto
  root = Tk()
  root.title("os")
  bombPhoto = PhotoImage(file = "bombdodger2.gif")
  bombdodger = Button(root, image = bombPhoto, command=lambda: bombdodge(user)).grid(row=0,column=0)
  bomblabel = Label(root, text="bombdodger").grid(row=1, column=0)
  wordPhoto = PhotoImage(file = "notepadIMAGE.gif")
  wordButton = Button(root, image = wordPhoto, command=word).grid(row=2,column=0)
  wordlabel = Label(root, text="notepad--").grid(row=3, column=0)

  Tphoto = PhotoImage(file = "translate.gif")
  Tbutton = Button (root, image = Tphoto, command=translate).grid(row=4,column=0)
  Tlabel = Label(root, text="Translate").grid(row=6, column=0)
  
  root.mainloop()

word()