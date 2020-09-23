#Spherical Shape
import turtle as tur

tur.speed(0)
tur.bgcolor("black")
colors=["white","gray"]
#loop for iteration
for color in range(120):
    #set pencolor for draw the spher
    tur.pencolor(colors[color%2])
    #set the width
    tur.width(color/250+1)
    #forward movement
    tur.forward(color)
    #left rotation
    tur.left(30)
#closing part
tur.end_fill()