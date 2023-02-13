import data_base as d_b
import create_screen as c_screen
import object_for_draw as ob_draw
import turtle 


def horizontal_victory(value, x, y, start, stop):
    count_score = 0
    for number in range(start, stop):
        if d_b.komirka[number] == value:
            count_score += 1

    if count_score == 3 and value == 1:
        d_b.finish[0] = False
        ob_draw.draw_line(x, y, angle = 0, step = 200)
        ob_draw.win(50,0,1)
        
    elif count_score == 3 and value == 2:
        d_b.finish[0] = False
        ob_draw.draw_line(x, y, angle = 0, step = 200)
        ob_draw.win(50,0,2)
        
        
def vertical_victory(start_cell, value, x, y):
    count_score = 0
    for count in range(3):
        if d_b.komirka[start_cell] == value:
            count_score += 1
            start_cell += 3

    if count_score == 3 and value == 1:
        d_b.finish[0] = False
        ob_draw.draw_line(x, y, angle = 90, step = 200)
        ob_draw.win(50,0,1)
        
        
    elif count_score == 3 and value == 2:
        d_b.finish[0] = False
        ob_draw.draw_line(x, y, angle = 90, step = 200)
        ob_draw.win(50,0,2)
        
        
def diagonal_victory(value):
    if d_b.komirka[0] == value and d_b.komirka[4] == value and d_b.komirka[8] == value:
        if value == 1:
            ob_draw.draw_line(x = -50, y = 50, angle = 45, step = (70 * 4))
            ob_draw.win(50,0,1)
        elif value == 2:
            ob_draw.draw_line(x = -50, y = 50, angle = 45, step = (70 * 4))
            ob_draw.win(50,0,2)
        d_b.finish[0] = False
        
    elif d_b.komirka[2] == value and d_b.komirka[4] == value and d_b.komirka[6] == value:
        if value == 1:
            ob_draw.draw_line(x = 150, y = 50, angle = 135, step = (70 * 4))
            ob_draw.win(50,0,1)
        elif value == 2:
            ob_draw.draw_line(x = 150, y = 50, angle = 135, step = (70 * 4))
            ob_draw.win(50,0,2)
        d_b.finish[0] = False
        
    