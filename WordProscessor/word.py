from tkinter import *

fileName = ""

def writeOpenFile(e, top):
  global fileName
  fileName = e.get()
  global t
  filePath = "WordProscessor/" + fileName
  if filePath == "word.py":
    exit("You cannot access that file.")
  with open(filePath, "r") as file:
    text = file.read()
  t.delete("1.0", END)
  t.insert("1.0", text)
  close_win(top)
  global root
  string = "Notepad -- - " + fileName
  root.title(string)
def save():
  global text
  global fileName
  filePath = "WordProscessor/" + fileName
  with open(filePath, "w") as file:
    file.write(text)
  global root
  string = "Notepad -- - " + fileName
  root.title(string)
def close_win(top):
  top.destroy()
def insert_val(e, top):
  global fileName
  fileName = e.get()
  if fileName == "word.py":
    exit("You cannot access that file")
  close_win(top)
  save()
def add_extension(extension):
  global entry
  entry.insert(len(entry.get()), extension)
def popupwin(action):
  top = Toplevel(root)
  top.geometry("750x250")
  global entry
  entry= Entry(top, width= 25)
  entry.pack()
  ttwo = Text(top, height = 10)
  ttwo.pack()
  from os import listdir
  from os.path import isfile, join
  files = [f for f in listdir("/home/runner/Doors-OS/WordProscessor/") if isfile(join("/home/runner/Doors-OS/WordProscessor/", f))]
  if "word.py" in files:
    files.remove("word.py")
  string = "\n".join(files)
  ttwo.insert("1.0", string)
  ttwo.config(state=DISABLED)
  if action == "save":
    Button(top,text= "Save", command= lambda:insert_val(entry, top)).pack(pady= 5,side=TOP)
    Button(top,text= "text file", command= lambda:add_extension(".txt")).pack(pady= 5,side=TOP)
    Button(top,text= "python file", command= lambda:add_extension(".py")).pack(pady= 5,side=TOP)
  elif action == "open":
    Button(top,text= "Open", command= lambda:writeOpenFile(entry, top)).pack(pady= 5,side=TOP)

def saveas():
  global t
  global text
  text = t.get("1.0", END)
  if text == "word.py":
    exit("You cannot open that file")
  else:
    popupwin("save")
def openFile():
  popupwin("open")

def start():
  global root, b2, b, t
  root = Tk()
  root.title("Notepad-- - unnamed")
  
  b2 = Button(root, text="Save as", command=saveas)
  b2.grid(row=0, column=0)
  b = Button(root, text="Open", command=openFile)
  b.grid(row=0, column=1)
  t = Text(root, height=50, width=100)
  t.grid(row=1, column=0, columnspan=50)
  
  root.mainloop()