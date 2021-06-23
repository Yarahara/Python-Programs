#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 02/13/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 06
#############################################

import turtle
wn=turtle.Screen()
g=turtle.Turtle()
g.begin_fill()

sides=int(input("How many sides does your polygon have in numbers?"))
length=float(input("What is the length of your polygon?"))
colorline=input("What is the color of your polygon in hex or rgb form?")
colorin=input("What is the interior color of your polygon in hex or rgb form?")
for i in range(sides):
    g.color(colorline,colorin)
    g.forward(sides)
    g.left(360/sides)
    
g.end_fill()
    
