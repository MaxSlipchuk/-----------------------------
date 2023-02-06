import draw_cross
import draw_zero
import data_base
import win_lose as w_l

def who_turn(x, y, index):
    if data_base.step[0] == "cross" and data_base.komirka[index] == 0:
        draw_cross.draw_cross(x, y)
        data_base.step[0] = "zero"
        data_base.komirka[index] = 1
    elif data_base.step[0] == "zero" and data_base.komirka[index] == 0:
        draw_zero.draw_zero(x, y)
        data_base.step[0] = "cross"
        data_base.komirka[index] = 2