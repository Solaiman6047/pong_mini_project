#made by:[hana mohamed solaiman,malak alaa hassan,jannat abd ellatif]
import turtle
import time
import random
# Background screen set up
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("PONG GAME")
wn.setup(width=800, height=600)
wn.tracer(0)
# Score variables
score_1 = 0
score_2 = 0
winning_score=1

# Scoring system
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("You: 0  Computer: 0", align='center', font=('courier', 24, 'normal'))
#function to move the ball
def ball_movement():
    y=ball.ycor()
    x=ball.xcor()
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)

 #bouncing the ball against the wall  
def ball_bouncing():
    global score_1,score_2
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:  
        ball.goto(0,0)
        ball.dx *= -1
        score_1+=1
        pen.clear()
        pen.write(f"You: {score_1}  Computer: {score_2}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
        winning()
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2+=1
        pen.clear()
        pen.write(f"You: {score_1}  Computer: {score_2}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
        winning()

def winning():
    if score_1>=winning_score:
        pen.clear()
        pen.write('YOU WIN :)', align='center', font=('courier', 30, 'normal'))
        wn.update()  
        time.sleep(3)
        pen.clear()
        restart()
        
        
    elif score_2>=winning_score: 
        pen.clear()
        pen.write('GAME OVER :(', align='center', font=('courier', 30, 'normal'))
        wn.update()
        time.sleep(3)
        pen.clear()
        restart()
        
        
def restart():
    global score_1, score_2
    score_1 = 0
    score_2 = 0
    ball.goto(0, 0)
    ball.dx = 2.5
    ball.dy = 2.5
    pen.clear()
    pen.write(f"You: {score_1}  Computer: {score_2}".format(score_1,score_2),align='center',font=('courier',23,'normal'))
        
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
    if y>250:
        y=250
    paddle_a.sety(y)
    
#function to move padel_a down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    if y<-250:
        y=-250
    paddle_a.sety(y)

#function to move padel_b up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=8
    if y>250:
        y=250
    paddle_b.sety(y)

#function to move padel_b down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=8
    if y<-250:
        y=-250
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




# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(5,1)
paddle_a.color("blue")
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
ball.dx=2.5
ball.dy=2.5
    
#press Up to move padel_a up
wn.listen()
wn.onkeypress(paddle_a_up,"Up")

#press Down to move padel_a down
wn.listen()
wn.onkeypress(paddle_a_down,"Down")

#ai movement
def ai_movement():
    offset=35
    if ball.heading()<90 or ball.heading()>270:
        target_y=calculate_ball_trajectory()[-1]
        if random.random()<0.4:
         if target_y>paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()+5)
         elif target_y<paddle_b.ycor()+offset:
            paddle_b.sety(paddle_b.ycor()-5)
    if paddle_b.ycor() > 250:
            paddle_b.sety(250)
    elif paddle_b.ycor() < -250:
            paddle_b.sety(-250)

# Main game loop
while True:
    calculate_ball_trajectory()
    ai_movement()
    ball_movement()
    ball_bouncing()
    ball_and_paddle()
    wn.update()  
    time.sleep(0.01)  