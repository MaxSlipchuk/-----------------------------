from draw_table import*
from draw_cross import*
from draw_zero import*

draw_table(-100,100)

def run_game():

    komirka = [
        0, 0, 0, 
        0, 0, 0, 
        0, 0, 0,
        ]

    game = True
    while game == True:
        whos_step = int(input("Хто ходить? 1 - Хрестик, 2 - Нулик. "))        
        if whos_step == 1:
            step = int(input("Введи число від 1 до 9, де 1 - верхній лівий кут, а 9 - правий нижній. "))
            if step == 1 and komirka[step - 1] == 0:
                draw_cross(-100,100)
                komirka[0] += 1
            elif step == 2 and komirka[step - 1] == 0:
                draw_cross(0,100)
                komirka[1] += 1
            elif step == 3 and komirka[step - 1] == 0:
                draw_cross(100,100)
                komirka[2] += 1
            elif step == 4 and komirka[step - 1] == 0:
                draw_cross(-100,0)
                komirka[3] += 1
            elif step == 5 and komirka[step - 1] == 0:
                draw_cross(0,0)
                komirka[4] += 1
            elif step == 6 and komirka[step - 1] == 0:
                draw_cross(100,0)
                komirka[5] += 1
            elif step == 7 and komirka[step - 1] == 0:
                draw_cross(-100,-100)
                komirka[6] += 1
            elif step == 8 and komirka[step - 1] == 0:
                draw_cross(0,-100)
                komirka[7] += 1
            elif step == 9 and komirka[step - 1] == 0:
                draw_cross(100,-100)
                komirka[8] += 1
            else:
                print("Комірка зайнята")

        if whos_step == 2:
            step = int(input("Введи число від 1 до 9, де 1 - верхній лівий кут, а 9 - правий нижній."))
            if step == 1 and komirka[step - 1] == 0:
                draw_zero(-100,100)
                komirka[0] += 1
            elif step == 2 and komirka[step - 1] == 0:
                draw_zero(0,100)
                komirka[1] += 1
            elif step == 3 and komirka[step - 1] == 0:
                draw_zero(100,100)
                komirka[2] += 1
            elif step == 4 and komirka[step - 1] == 0:
                draw_zero(-100,0)
                komirka[3] += 1
            elif step == 5 and komirka[step - 1] == 0:
                draw_zero(0,0)
                komirka[4] += 1
            elif step == 6 and komirka[step - 1] == 0:
                draw_zero(100,0)
                komirka[5] += 1
            elif step == 7 and komirka[step - 1] == 0:
                draw_zero(-100,-100)
                komirka[6] += 1
            elif step == 8 and komirka[step - 1] == 0:
                draw_zero(0,-100)
                komirka[7] += 1
            elif step == 9 and komirka[step - 1] == 0:
                draw_zero(100,-100)
                komirka[8] += 1
            else:
                print("Комірка зайнята")

run_game()


