#Jonathon Thompson

#4/7/2024

#P4LAB1

#This code will draw a circle and a square


import turtle
win = turtle.Screen()   #allows turtle to be used
sh = turtle.Turtle()
j = turtle.Turtle()
t = turtle.Turtle()

for sq in range(4): #makes square
    sh.forward(200)
    sh.right(90)

for tri in range(3):  #makes triangle
    sh.forward(200)
    sh.left(120)




j.right(180)
j.up()
j.forward(400)
j.down()
j.right(90)
j.forward(50)
j.right(90)
j.forward(200)
j.right(90)
j.forward(50)
j.right(90)
j.forward(80)
j.left(90)
j.forward(100)                #makes the J in my intitals

for curve_1 in range(90):
    j.forward(1)
    j.right(1)

j.forward(60)
j.right(90)
j.forward(40)
j.right(90)
j.forward(15)

for curve_2 in range(90):
    j.forward(1)
    j.left(1)

j.forward(60)
j.left(90)
j.forward(80)



t.right(180)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(70)
t.right(90)
t.forward(200)
t.left(90)
t.forward(60)
t.left(90)
t.forward(200)
t.right(90)
t.forward(70)
t.left(90)
t.forward(50)



