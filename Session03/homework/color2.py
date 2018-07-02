from turtle import *

speed(1)
colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(3, 7):
    for j in range(i):
        forward(100)
        left(360/i)
        color(colors[i - 3])

mainloop()