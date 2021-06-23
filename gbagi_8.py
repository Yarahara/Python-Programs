#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 02/28/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 08
#############################################

import turtle
import random
wn=turtle.Screen()
wn.bgcolor("Lightblue")

bo=turtle.Turtle()
bo.color("black")
bo.shape("turtle")
bo.pensize(4)
bo.up()
bo.goto(-300,40)

ed=turtle.Turtle()
ed.color("red")
ed.shape("turtle")
ed.pensize(4)
ed.up()
ed.goto(-300,0)

aj=turtle.Turtle()
aj.color("darkslateblue")
aj.shape("turtle")
aj.pensize(4)
aj.up()
aj.goto(-300,-40)

cj=turtle.Turtle()
cj.color("grey")
cj.pensize(3)
cj.speed("fastest")
cj.hideturtle()
cj.up()

cj.goto(-300,60)
cj.down()
cj.forward(600)

cj.up()
cj.goto(-300,20)
cj.down()
cj.forward(600)

cj.up()
cj.goto(-300,-20)
cj.down()
cj.forward(600)

cj.up()
cj.goto(-300,-60)
cj.down()
cj.forward(600)

cj.up()
cj.goto(295,65) #
cj.color("darkcyan")
cj.down()
cj.left(90)
cj.forward(20)

cj.up()
cj.goto(300,65)#
cj.down()
cj.forward(40)

cj.left(90)
cj.forward(65)

cj.left(90)
cj.forward(20)
cj.left(90)
cj.forward(60)

cj.up()
cj.goto(270,85)
cj.write("FINISH", False, 'center', font=('Web',18,'bold'))

cj.color("grey")
cj.goto(295,-60)
cj.down()
cj.left(90)
cj.forward(120)
for race in range(105):
    bo.forward(random.randint(1,10))
    ed.forward(random.randint(1,10))
    aj.forward(random.randint(1,10))

wn.exitonclick()
