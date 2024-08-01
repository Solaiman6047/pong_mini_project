#function to move the ball
def ball_movement():
    y=ball.ycor()
    x=ball.xcor()
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)

 #bouncing the ball against the wall  
def ball_bouncing():
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:  
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        
#function to bounce the ball against the paddle:
def ball_and_paddle():
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
def move_ball():
    ball.forward(10)
    
#function to move padel_a up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
#function to move padel_a down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#function to move padel_b up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=8
    paddle_b.sety(y)

#function to move padel_b down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=8
    paddle_b.sety(y)

#ai implementation
def calculate_ball_trajectory():
    width=800
    initial_ball_pos=ball.pos()
    initial_ball_angle=ball.heading()
    ball.setheading(ball.heading()%360)
    if ball.heading()<90 or ball.heading>270:
        while ball.xcor()<width//2-75:
            ball_movement()
            move_ball()
            ball_bouncing()
    x,y=ball.pos()
    ball.setpos(initial_ball_pos)
    ball.setheading(initial_ball_angle)
    return x,y

import turtle
import time

# Background screen set up
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("PONG GAME")
wn.setup(width=800, height=600)
wn.tracer(0)


# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(5,1)
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(5,1)
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx=2
ball.dy=2
    
#press Up to move padel_a up
wn.listen()
wn.onkeypress(paddle_a_up,"Up")

#press Down to move padel_a down
wn.listen()
wn.onkeypress(paddle_a_down,"Down")

#ai movement
def ai_movement():
    offset=10
    if ball.heading()<90 or ball.heading()>270:
        target_y=calculate_ball_trajectory()[-1]
        if target_y>paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()+5)
        elif target_y<paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()-5)

# Main game loop
while True:
    calculate_ball_trajectory()
    ai_movement()
    ball_movement()
    ball_bouncing()
    ball_and_paddle()
    wn.update()  
    time.sleep(0.01)  