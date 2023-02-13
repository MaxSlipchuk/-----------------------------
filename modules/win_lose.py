import modules.data_base as m_d_b
import modules.object_for_draw as m_ob_draw
import turtle

restart = True


def horizontal_victory(value, x, y, start, stop):
    count_score = 0
    for number in range(start, stop):
        if m_d_b.komirka[number] == value:
            count_score += 1

    if count_score == 3 and value == 1:
        m_d_b.finish[0] = False
        m_ob_draw.draw_line(x, y, angle = 0, step = 200)
        m_ob_draw.win(50,0,1)
        
    elif count_score == 3 and value == 2:
        m_d_b.finish[0] = False
        m_ob_draw.draw_line(x, y, angle = 0, step = 200)
        m_ob_draw.win(50,0,2)

          
def vertical_victory(start_cell, value, x, y):
    count_score = 0
    for count in range(3):
        if m_d_b.komirka[start_cell] == value:
            count_score += 1
            start_cell += 3

    if count_score == 3 and value == 1:
        m_d_b.finish[0] = False
        m_ob_draw.draw_line(x, y, angle = 90, step = 200)
        m_ob_draw.win(50,0,1)
        
    elif count_score == 3 and value == 2:
        m_d_b.finish[0] = False
        m_ob_draw.draw_line(x, y, angle = 90, step = 200)
        m_ob_draw.win(50,0,2)
        
        
def diagonal_victory(value):
    if m_d_b.komirka[0] == value and m_d_b.komirka[4] == value and m_d_b.komirka[8] == value:
        if value == 1:
            m_ob_draw.draw_line(x = -50, y = 50, angle = 45, step = (70 * 4))
            m_ob_draw.win(50,0,1)
        elif value == 2:
            m_ob_draw.draw_line(x = -50, y = 50, angle = 45, step = (70 * 4))
            m_ob_draw.win(50,0,2)
        m_d_b.finish[0] = False
        
    elif m_d_b.komirka[2] == value and m_d_b.komirka[4] == value and m_d_b.komirka[6] == value:
        if value == 1:
            m_ob_draw.draw_line(x = 150, y = 50, angle = 135, step = (70 * 4))
            m_ob_draw.win(50,0,1)
        elif value == 2:
            m_ob_draw.draw_line(x = 150, y = 50, angle = 135, step = (70 * 4))
            m_ob_draw.win(50,0,2)
        m_d_b.finish[0] = False
        
    