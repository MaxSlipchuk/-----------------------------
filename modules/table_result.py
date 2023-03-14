import turtle
import json
import modules.save_game as m_s_game

# черепашка відповідає за малювання таблиці
t9 = turtle.Turtle()
t9.speed(0)
t9.hideturtle()
t9.color("brown","lightyellow")
t9.width(4)

# черепашка відповідає за заголовок таблиці
t10 = turtle.Turtle()
t10.speed(0)
t10.color("brown")
t10.hideturtle()

# черепашка відповідає за імена гравців та рахунок
t11 = turtle.Turtle()
t11.speed(0)
t11.color("brown")
t11.hideturtle()

count_write = 0

def table_result(x, y):
    # створення функції, яка малює таблицю результатів 
    t9.penup()
    t9.goto(x,y)
    t9.pendown()
    t9.begin_fill()
    for count in range(4):
        t9.forward(200)
        t9.right(90)
    t9.end_fill()

    # створення функції яка відповідає за заголовок на таблиці
    t10.penup()
    t10.goto(x + 100, y - 75)
    t10.pendown()
    t10.write("""РЕЗУЛЬТАТ
      ГРИ""", font = ("Verdana", 20, "bold"), align = "center")
    global count_win
    # створення функції, яка відповідає за напис гравців з json
    
    def count_win():
        global count_write
        t11.penup()
        t11.goto(x + 15, y - 125)

        with open(m_s_game.path, "r") as file:
            names = json.load(file)
        if count_write > 0:
            t11.reset()

        if count_write == 0 or count_write > 0:
            t11.speed(0)
            t11.color("brown")
            t11.hideturtle()

            t11.penup()
            t11.goto(x + 15, y - 125)
            t11.write(names["player_1"]["name"], font = ("Verdana", 15, "bold"), align = "left")
            t11.goto(x + 165, y - 125)
            t11.write(names["player_1"]["count_win"], font = ("Verdana", 12, "bold"), align = "left")
            t11.goto(x + 15, y - 165)
            t11.write(names["player_2"]["name"], font = ("Verdana", 15, "bold"), align = "left")
            t11.goto(x + 165, y - 165)
            t11.write(names["player_2"]["count_win"], font = ("Verdana", 12, "bold"), align = "left")
            count_write += 1
    # count_win()



# turtle.done()
        



# draw_table_result(-300,100)
# write_table_result(-200,25)
# write_name_players(-280,-25)




