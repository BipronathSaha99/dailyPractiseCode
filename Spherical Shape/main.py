#Spherical Shape
import turtle as tur
#set a window
sphere=tur.Turtle()
sphere.speed(0)
tur.bgcolor("black")
#create a color list
color=["white"]
#iteration
for i in range(60):
    sphere.pencolor(color[i%1])
    sphere.width(i/250+1)
    #to move with forward direction
    sphere.forward(i)
    sphere.left(30)
sphere.end_fill()
