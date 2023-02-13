import draw_cross
import draw_zero
import data_base as d_b
import win_lose as w_l

def who_turn(x, y, index):
    if d_b.step[0] == "cross" and d_b.komirka[index] == 0 and d_b.finish[0]:
        draw_cross.draw_cross(x, y)
        d_b.step[0] = "zero"
        d_b.komirka[index] = 1

        w_l.horizontal_victory(1, -50, 50, 0, 3)
        w_l.horizontal_victory(1, -50, -50, 3, 6)
        w_l.horizontal_victory(1, -50, -150, 6, 9)

        w_l.vertical_victory(0, 1, -50, 50)
        w_l.vertical_victory(1, 1, 50, 50)
        w_l.vertical_victory(2, 1, 150, 50)

        w_l.diagonal_victory(1)
    
    elif d_b.step[0] == "zero" and d_b.komirka[index] == 0 and d_b.finish[0]:
        draw_zero.draw_zero(x, y)
        d_b.step[0] = "cross"
        d_b.komirka[index] = 2

        w_l.horizontal_victory(2,-50, 50, 0, 3)
        w_l.horizontal_victory(2,-50, -50, 3, 6)
        w_l.horizontal_victory(2,-50, -150, 6, 9)

        w_l.vertical_victory(0,2, -50,50)
        w_l.vertical_victory(1,2, 50,50)
        w_l.vertical_victory(2,2, 150,50)

        w_l.diagonal_victory(2)
        
    