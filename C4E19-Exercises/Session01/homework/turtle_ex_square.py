from turtle import *

shape("turtle")
speed(1)
color("green","yellow")

begin_fill()
for i in range(4):
    fd(100)
    lt(90)
end_fill()

mainloop()
