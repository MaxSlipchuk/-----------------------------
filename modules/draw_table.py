import turtle

t1 = turtle.Turtle() 
t1.speed(0)
t1.width(4)
t1.hideturtle()

def draw_table(x, y):
    def square():
        for count in range(4):
            t1.forward(100)
            t1.right(90)

    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    x_cor = x
    y_cor = y
    for count in range (3):
        for count in range(3):
            square()
            x_cor += 100
            t1.goto(x_cor, y_cor)
        x_cor -= 300
        y_cor -= 100
        t1.penup()
        t1.goto(x_cor, y_cor)
        t1.pendown()


        
