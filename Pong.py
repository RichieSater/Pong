import turtle

wn = turtle.Screen()
wn.title("Pong by Richie")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #Done for speed

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Sets speed to maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #stops turtle from drawing line
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Sets speed to maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #stops turtle from drawing line
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #Sets speed to maximum
ball.shape("square")
ball.color("white")
ball.penup() #stops turtle from drawing line
ball.goto(0,0)
ball.dx = .05
ball.dy = .05

# Functions
def paddle_a_up():
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

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



#Main Game Loop
while True:
    wn.update()

    #Move Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Checking
    #Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #Left and Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
    
    #Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

#29:16
#https://www.youtube.com/watch?v=XGf2GcyHPhc
#https://www.youtube.com/watch?v=9zOo4JkZgSI