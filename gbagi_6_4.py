#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 02/13/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 06
#############################################

import turtle
wn= turtle.Screen()
wn.bgcolor("lightgreen")
bb=turtle.Turtle()
bb.color("blue")
bb.shape("turtle")
bb.pensize(3)
bb.up()

for i in range(12):
    bb.forward(50)
    bb.down()
    bb.forward(10)
    bb.up()
    bb.forward(20)
    bb.stamp()
    bb.bk(80)
    bb.right(30)
    

