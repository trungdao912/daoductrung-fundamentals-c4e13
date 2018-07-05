from turtle import *

color("red")
speed(1)


for i in range (0, 100, 2) :
    for j in range (4) :
        forward(10 + i)
        left(90)
    left(10)

mainloop()