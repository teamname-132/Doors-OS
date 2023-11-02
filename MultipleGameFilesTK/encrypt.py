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