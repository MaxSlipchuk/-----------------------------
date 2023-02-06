import turtle 

t2 = turtle.Turtle() 
t2.color("red")
t2.width(2)
t2.speed(0)
t2.hideturtle()

def draw_cross(x, y):
    t2.penup()
    t2.goto(x, y)
    t2.pendown()
    x_cor = x + 100
    y_cor = y - 100
    
    t2.goto(x_cor, y_cor)
    t2.penup()
    t2.goto(x_cor, y_cor + 100)
    t2.pendown()
    t2.goto(x_cor - 100, y_cor)


