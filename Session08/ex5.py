from turtle import *

def draw_star(x, y, length,star_color):
    color("green", star_color)
    count = 0
    angle = 144
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
    mainloop()


draw_star(100, 10, 100, "red")
mainloop()