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