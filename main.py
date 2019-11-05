import turtle
import random
import time

WIDTH = 700
HEIGHT = 700

root = turtle.Screen()
root.setup(WIDTH,HEIGHT)
root.bgcolor('black')
root.title('Snake by raphtlw')

border = 330

snake = turtle.Turtle()
snake.penup()
snake.speed(0)
snake.color('white')
snake.shape('square')
snake.shapesize(1,1)
snake.goto(0,0)

food = turtle.Turtle()
food.penup()
food.speed(0)
food.color('red')
food.shape('square')
food.shapesize(0.5,0.5)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color('white')
pen.shape('square')
pen.hideturtle()
pen.goto(0,100)

segments = []
forward = 9

def moveup():
    snake.seth(90)

def movedown():
    snake.seth(270)

def moveright():
    snake.seth(0)

def moveleft():
    snake.seth(180)

# keybindings
root.onkeypress(moveup, 'w')
root.onkeypress(movedown, 's')
root.onkeypress(moveright,'d')
root.onkeypress(moveleft, 'a')
root.listen()

while True:  # gameloop
    root.update()
    snake.forward(forward)  # moving the snake forward
    if snake.ycor() > border or snake.ycor() < -border:
        break
    if snake.xcor() > border or snake.xcor() < -border:
        break
    if snake.distance(food) < 10:
        foodx = random.randint(-border,border)
        foody = random.randint(-border,border)  # random integer to set random position for snake food
        food.goto(foodx,foody)

        for i in range(0,5):
            # turtle 'body'
            new_segment = turtle.Turtle()
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('white')
            segments.append(new_segment)
            new_segment.showturtle()

        forward += 0.2  # += is used to add to a variable

    for index in range(len(segments)-1,0,-1):  # setting the snake body blocks to be below the snake head
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

# game over
pen.write('Game Over', move=False, align='center', font=('Inter', 20))
time.sleep(1)
exit()