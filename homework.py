import turtle
sc = turtle.Screen()
turtle.Screen().bgcolor("yellow")
sc.setup(300,500)
turtle.title("Welcome to the canvas!")
pen = turtle.Turtle()
pen.forward(100)

#rectangle
pen.right(90)
pen.down(200)
pen.left(200)
pen.up(200)
pen.penup()

pen.pendown()
turtle.done()


import turtle

sc = turtle.Screen()
sc.bgcolor("yellow")
sc.setup(300, 500)
turtle.title("Welcome to the canvas, triangle drawing")

#triangle
pen = turtle.Turtle()
pen.shape("turtle")

for i in range(3):
    pen.forward(100)
    pen.right(120)

turtle.done()



import turtle 
sc = turtle.Screen()
sc.bgcolor("yellow")
sc.setup(300, 500)
turtle.title("Welcome to the canvas, hexagon")

#hex
pen = turtle.Turtle()
pen.shape("turtle")
pen.forward(100)
pen.right(60)

pen.forward(100)
pen.right(60)

pen.forward(100)
pen.right(60)

pen.forward(100)
pen.right(60)

pen.forward(100)
pen.right(60)

pen.forward(100)
pen.right(60)

turtle.done()


