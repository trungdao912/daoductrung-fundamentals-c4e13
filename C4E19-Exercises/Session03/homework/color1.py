from turtle import *
speed(1)

colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(len(colors)):
    for j in range(2):
        fillcolor(colors[i])
        begin_fill()
        forward(50)
        left(90)
        forward(100)
        left(90)
        end_fill()
    forward(50)

mainloop()