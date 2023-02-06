import turtle

t3 = turtle.Turtle()
t3.color('darkblue')
t3.width(2)
t3.speed(0) 
t3.hideturtle()

def draw_zero(x, y):
    
    t3.penup()
    t3.goto(x + 50, y)
    t3.left(180)
    t3.pendown()
    t3.circle(50)
    t3.left(180)

    

