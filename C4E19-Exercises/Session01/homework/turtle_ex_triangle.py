from turtle import *

shape("turtle")
speed(-1)
color("green", "yellow")

begin_fill()
for i in range(3):
    fd(100)
    lt(120)
end_fill()

mainloop()