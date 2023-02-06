import data_base as db
import turtle

t4 = turtle.Turtle()
t4.width(5)
t4.color("darkgreen")
t4.speed(0)
t4.hideturtle()

def draw_line(x, y):
    t4.penup()
    t4.goto(x,y)
    t4.pendown()
    t4.forward(200)

def horizontal_victory(value, x, y, start, stop):
    count_score = 0
    for number in range(start, stop):
        if db.komirka[number] == value:
            count_score += 1
    if count_score == 3:
        draw_line(x, y)
    
def vertical_victory (value, x, y, start, stop):
    count_score = 0

            
            
    
    