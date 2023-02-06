import player_way as p_way
import data_base 
import win_lose as w_l

def click_cell(x, y):
    # створення першого рядка
    if y > 0 and y < 100:
        # створення першої комірки
        if x > -100 and x < 0:
            p_way.who_turn(-100,100,0)
        # створення другої комірки
        elif x > 0 and x < 100:
            p_way.who_turn(0,100,1)
        # створення третьої комірки
        elif x > 100 and x < 200:
            p_way.who_turn(100,100,2)
        w_l.horizontal_victory(1,-50, 50, 0, 3)
        w_l.horizontal_victory(2,-50, 50, 0, 3)
    # створення другого рядка
    elif y > -100 and y < 0:
        if x > -100 and x < 0:
            p_way.who_turn(-100,0,3)
        elif x > 0 and x < 100:
            p_way.who_turn(0,0,4)
        elif x > 100 and x < 200:
            p_way.who_turn(100,0,5)
        w_l.horizontal_victory(1,-50, -50, 3, 6)
        w_l.horizontal_victory(2,-50, -50, 3, 6)
    # створення третього рядка
    elif y > -200 and y < -100:
        if x > -100 and x < 0:
            p_way.who_turn(-100,-100,6)
        elif x > 0 and x < 100:
            p_way.who_turn(0,-100,7)
        elif x > 100 and x < 200:
            p_way.who_turn(100,-100,8)
        w_l.horizontal_victory(1,-50, -150, 6, 9)
        w_l.horizontal_victory(2,-50, -150, 6, 9)


        
