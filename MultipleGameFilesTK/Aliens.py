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