'''
import tkinter
from tkinter import *
from translate import Translator
import time as T
from tkinter import messagebox

def Translate():
  global Screen, InputLanguageChoice, TranslateLanguageChoice, TextVar, OutputVar
  translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
  Translation = translator.translate(TextVar.get())
  OutputVar.set(Translation)

def start():
  global Screen, InputLanguageChoice, TranslateLanguageChoice, TextVar, OutputVar
  Screen = Tk()
  Screen.title("Language Traslator ")
  

  
  InputLanguageChoice = StringVar()
  TranslateLanguageChoice = StringVar()
  LanguageChoices = {'English','French','German','Spanish'}
  InputLanguageChoice.set('English')
  TranslateLanguageChoice.set('French')
  
  InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
  Label(Screen,text="Choose a Language").grid(row=0,column=1)
  InputLanguageChoiceMenu.grid(row=1,column=1)
   
  
  NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
  Label(Screen,text="Translated Language").grid(row=0,column=2)
  
  NewLanguageChoiceMenu.grid(row=1,column=2)
  
  Label(Screen,text="Enter Text").grid(row=2,column =0)
  
  TextVar = StringVar()
  TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
   
  Label(Screen,text="Output Text").grid(row=2,column =2)
  OutputVar = StringVar()
  TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
   
  
  B = Button(Screen,text="Translate",command=Translate, relief=GROOVE).grid(row=3,column=1,columnspan=3)
  Screen.mainloop()
'''
#messige = 'Downloding data'
#tkinter.messagebox.showinfo(Translator,messige)

