from linecache import getline
from tkinter import Label,Entry,Tk,Button
import json
import bcrypt
import homeScreen

with open ("users.json", "r") as file:
  users = json.loads(file.read())

def signUp():
  global hoorayLabel
  hoorayLabel.config(text="We have signed you up because you \n didn't have an account")

def screen():
  global signinRoot
  signinRoot = Tk()
  signinRoot.title("os")
  global nameLabel
  nameLabel = Label(signinRoot, text="Name: ")
  nameLabel.grid(row=0, column=0)
  global nameInput
  nameInput = Entry(signinRoot)
  nameInput.grid(row=0, column=1)
  global passLabel
  passLabel = Label(signinRoot, text="Password: ")
  passLabel.grid(row=1, column=0)
  global passInput
  passInput = Entry(signinRoot)
  passInput.grid(row=1,column=1)
  global hoorayLabel
  hoorayLabel = Label(signinRoot, text="Waiting on input...")
  hoorayLabel.grid(row=4,column=0,columnspan=2)
  global submit
  submit = Button(signinRoot, text="Submit", command=submit)
  submit.grid(row=3,column=0)
  signinRoot.mainloop()

def submit():
  global users
  global signinRoot
  global hoorayLabel
  global user
  global username
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
    signinRoot.destroy()
    homeScreen.generate(username)
  else:
    hoorayLabel.config(text="Wrong password.")

def getStuff(thing):
  global user, users, username
  if thing == "user":
    return user
  elif thing == "users":
    return users
  elif thing == "username":
    return username