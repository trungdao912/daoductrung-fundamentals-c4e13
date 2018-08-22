from turtle import *

def draw_square(length, square_color):
    shape("turtle")
    speed(1)
    color("green", square_color)

    begin_fill()
    for i in range(4):
        fd(length)
        lt(90)
    end_fill()

    mainloop()

