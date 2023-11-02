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
