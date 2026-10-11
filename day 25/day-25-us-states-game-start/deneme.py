import turtle

t = turtle.Turtle()
t.penup()
print(t.pos())
t.write("A")
t.goto(100, 100)
print(t.pos())
t.write("B")

turtle.done()