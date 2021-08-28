import random
import turtle
import time
import pygame
from pygame import mixer

"""pygame.init()
mixer.music.load('bgm.mp3')
mixer.music.play(-1)"""

<<<<<<< HEAD
point = 0
high_score = 0

=======
>>>>>>> d069269fe8c9f9d8b4eefe57fc273968bb79d7fc
velocity = 0.10


window = turtle.Screen()
window.title('Snake Game')
window.bgcolor("pink")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("brown")
head.penup()
head.goto(0, 100)
head.direction = "stop"

bait = turtle.Turtle()
bait.speed(0)
bait.shape("circle")
bait.color("black")
bait.penup()
bait.shapesize(0.80, 0.80)
bait.goto(0, 0)

tails = []


board = turtle.Turtle()
board.speed(0)
board.penup()
board.hideturtle()
board.goto(-290, 265)
board.write("Score:0   High Score: 0", font=("Times New Roman", 24, "normal"))
    

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

while True:
    window.update()
   
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for tail in tails:
            tail.goto(1000, 1000)
        tails = []
        point = 0
        velocity = 0.10
        
        board.clear()
        board.write("Score: {}   High Score: {}".format(point, high_score), font=("Times New Roman", 24, "normal"))

    
        

    if head.distance(bait) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        bait.goto(x, y)

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("circle")
        new_tail.color("green")
        new_tail.penup()

        tails.append(new_tail)

        velocity = velocity + 0.0001
        point = point + 5

        if point > high_score:             
            high_score = point
            
        board.clear()
        board.write("Score: {}   High Score: {}".format(point, high_score), font=("Times New Roman", 24, "normal"))
        
    

    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()

    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            point = 0
            board.clear()
            board.write("Score: {}   High Score: {}".format(point, high_score), font=("Times New Roman", 24, "normal"))
            velocity = 0.15

    time.sleep(velocity)