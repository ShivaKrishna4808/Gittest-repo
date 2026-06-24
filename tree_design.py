import turtle

def draw_tree(branch_len,angle):
    if branch_len < 5:
        return
    t.forward(branch_len)
    t.right(angle)
    draw_tree(branch_len*0.75,angle)
    t.left(angle*2)
    draw_tree(branch_len*0.75,angle)
    t.right(angle)
    t.backward(branch_len)

screen = turtle.Screen()
screen.title("My Fractal Tree")
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.backward(300)
t.pendown()
draw_tree(100, 25)
screen.exitonclick()