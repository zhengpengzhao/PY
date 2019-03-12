#import turtle as t

import turtle as t

t.screensize(400, 400)

# 正方形
t.pensize(5)
t.penup()
t.goto(-350, 250)
t.pendown()
t.pencolor('green')
t.begin_fill()
t.fillcolor('green')
for i in range(4):
    t.forward(80)
    t.left(90)
t.end_fill()
t.done()
