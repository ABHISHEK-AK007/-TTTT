import turtle as t

t.speed(0)
t.bgcolor("black")
t.pencolor("blue")


def square(x, y):
    for j in range(4):
        t.forward(x)
        t.right(y)


for i in range(80):
    square(200, 90)
    t.right(5)
    t.circle(80)
    t.right(50)


t.hideturtle()
t.done()