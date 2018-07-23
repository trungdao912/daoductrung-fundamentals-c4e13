from turtle import *
import random

def draw_star(x, y, length,star_color):
    color("green", star_color)
    count = 0
    angle = 144
    speed(-1)
    begin_fill()
    penup()
    setpos(x, y)
    pendown()
    begin_fill()
    while count <= 5:
        forward(length)
        right(angle)
        count += 1
    end_fill()

for i in range(100):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length, "blue")

mainloop()