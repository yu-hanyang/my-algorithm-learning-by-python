import turtle

def tree(branch_len):
    if branch_len>5:
        t.forward(branch_len)
        t.right(60)
        tree(branch_len-15)
        t.left(120)
        tree(branch_len-15)
        t.right(60)
        t.backward(branch_len)

t=turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.hideturtle()
t.pencolor('green')
t.pensize(2)
tree(100)
turtle.done()