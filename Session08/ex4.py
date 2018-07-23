from turtle import *
shape("turtle")
speed(-1)

def draw_square(length, square_color):
    color("green", square_color)
    begin_fill()
    for i in range(4):
        fd(length)
        lt(90)
    end_fill()
    length += 1

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
