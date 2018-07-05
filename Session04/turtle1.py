from turtle import *


color("green")
speed(-1)


for i in range(100):
    for j in range(4):
        forward(100)
        left(90)
    left(360/100)

mainloop()