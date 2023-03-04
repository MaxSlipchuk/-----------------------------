import turtle
import json
import modules.save_game as m_s_game


# черепашка відповідає за переможну лінію
t4 = turtle.Turtle()
t4.width(7)
t4.color("darkgreen")
t4.speed(0)
t4.hideturtle()

# черепашка відповідає за малювання квадрату на якому буде писатись перемога
t5 = turtle.Turtle()
t5.width(5)
t5.color("black","lightyellow")
t5.speed(0)
t5.hideturtle()

# черепащка відповідає за напис ВІТАЮ
t6 = turtle.Turtle()
style_t6 = ("Verdana", 30, "bold")
t6.color("brown")
t6.hideturtle()

# черепашка выдповідає за напис (перемогли хрестики/нулики)
t7 = turtle.Turtle()
style_t7 = ("Verdana", 15, "bold")
t7.hideturtle()

def draw_line(x, y, angle,step):
    t4.right(angle)
    t4.penup()
    t4.goto(x,y)
    t4.pendown()
    t4.forward(step)
    t4.left(angle)

def square_winner():
    t5.penup()
    t5.goto(-50, 50)
    t5.pendown()
    t5.begin_fill()
    for i in range(4):
        t5.forward(200)
        t5.right(90)
    t5.end_fill()

def win(x, y, value):
    square_winner()
    t6.penup()
    t6.goto(x,y)
    t6.pendown()
    t6.write("ВІТАЮ", font = style_t6, align = "center")

    t7.penup()
    t7.goto(x,y - 65)
    t7.pendown()
    if value == 1:

        with open(m_s_game.path, "r") as file:
            winner = json.load(file)
            winner = winner["player_1"]

        t7.color("red")
        t7.write("""ПЕРЕМІГ
ГРАВЕЦЬ""", font = style_t7, align = "center")
        t7.penup()
        t7.goto(x, y - 100)
        t7.pendown()
        t7.write(f"'{winner}'", font = style_t7, align = "center")
    elif value == 2:

        with open(m_s_game.path, "r") as file:
            winner_1 = json.load(file)
            winner_1 = winner_1["player_2"]

        t7.color("dodgerblue")
        t7.write("""ПЕРЕМІГ
ГРАВЕЦЬ""", font = style_t7, align = "center")
        t7.penup()
        t7.goto(x, y - 100)
        t7.pendown()
        t7.write(f"'{winner_1}'", font = style_t7, align = "center")
    

