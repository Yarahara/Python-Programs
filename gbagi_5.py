#############################################
# Name: John Doe (substitute this with your name))
# Submission Date: 00/00/2020 (assignment due date)
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 05
#############################################


import turtle
import random
wn=turtle.Screen()

colors=["yellow"]

bb=turtle.Turtle()
bb.speed("fastest")
t=turtle.Turtle()
t.speed("fastest")
wn.bgcolor("#00001a")

for i in range(15):
    x=random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    y=random.randrange(200,400)
    size=random.randint(5,8)
    color=random.choice(colors)

    t.up()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color)
    t.begin_fill()
    t.down()

    for o in range(5):
        t.forward(size)
        t.left(225)
        t.forward(size)
        t.left(63)

    t.end_fill()

t.penup()
t.home()
t.left(180)
t.forward(200)
t.right(90)
t.forward(250)
t.pendown()

t.begin_fill()
t.color("white")
t.circle(50)
t.end_fill()


t.up()
t.home()

t.right(135)
t.forward(400)
t.right(165)

t.begin_fill()
t.color("lightgray")

t.down()
t.forward(600)

t.right(120)
t.forward(100)

t.left(127)
t.forward(170)

t.right(135)
t.forward(670)

t.right(114.6)
t.forward(680)

t.end_fill()

t.up()
t.home()

t.left(180)
t.forward(250)

t.right(90)
t.forward(100)

t.down()
t.color("yellow")
t.begin_fill()
t.hideturtle()

bb.up()
bb.goto(-500,-325)
bb.down()
bb.color("green")
bb.begin_fill()
bb.left(45)
bb.forward(100)
bb.right(90)
bb.forward(100)
bb.left(90)
bb.forward(100)
bb.right(90)
bb.forward(100)
for o in range(5):
    bb.left(90)
    bb.forward(100)
    bb.right(90)
    bb.forward(100)
    
bb.right(135)
bb.forward(1000)
bb.end_fill()
bb.backward(150)
bb.right(90)
bb.color("olivedrab")
bb.pensize(3)
bb.forward(100)

coco=["red","mediumvioletred","lightcoral","maroon","crimson","pink","palevioletred"]

bb.color(random.choice(coco))
bb.color("red")

bb.up()
bb.right(90)
bb.forward(95)
bb.down()
bb.left(90)

for o in range(20):
    bb.left(95)
    bb.forward(100)
    bb.right(90)
    bb.forward(100)
    bb.left(95)


bb.up()    
bb.goto(-13,-325)
bb.down()
bb.seth(0)
bb.left(90)
bb.color("olivedrab")
bb.forward(100)


bb.color("mediumvioletred")

bb.up()
bb.right(90)
bb.forward(95)
bb.down()
bb.left(90)

for o in range(20):
    bb.left(95)
    bb.forward(100)
    bb.right(90)
    bb.forward(100)
    bb.left(95)


bb.up()    
bb.goto(300,-325)
bb.down()
bb.seth(0)
bb.left(90)
bb.color("olivedrab")
bb.forward(100)


bb.color("lightcoral")

bb.up()
bb.right(90)
bb.forward(95)
bb.down()
bb.left(90)

for o in range(20):
    bb.left(95)
    bb.forward(100)
    bb.right(90)
    bb.forward(100)
    bb.left(95)

bb.up()    
bb.goto(-150,-325)
bb.down()
bb.seth(0)
bb.left(90)
bb.color("olivedrab")
bb.forward(100)


bb.color("maroon")

bb.up()
bb.right(90)
bb.forward(50)
bb.down()
bb.left(90)

for o in range(20):
    bb.left(95)
    bb.forward(50)
    bb.right(90)
    bb.forward(50)
    bb.left(95)

bb.up()    
bb.goto(120,-325)
bb.down()
bb.seth(0)
bb.left(90)
bb.color("olivedrab")
bb.forward(100)


bb.color("pink")

bb.up()
bb.right(90)
bb.forward(75)
bb.down()
bb.pensize(4)
bb.left(90)

for o in range(20):
    bb.left(95)
    bb.forward(75)
    bb.right(90)
    bb.forward(75)
    bb.left(95)

    
