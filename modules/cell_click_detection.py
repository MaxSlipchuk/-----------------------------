import modules.player_way as m_p_way
import modules.clear as m_clear
import modules.data_base as m_d_b

def click_cell(x, y):
    # створення першого рядка
    if y > 0 and y < 100:
        # створення першої комірки
        if x > -100 and x < 0:
            m_p_way.who_turn(-100,100,0)
        # створення другої комірки
        elif x > 0 and x < 100:
            m_p_way.who_turn(0,100,1)
        # створення третьої комірки
        elif x > 100 and x < 200:
            m_p_way.who_turn(100,100,2)
      
    # створення другого рядка
    elif y > -100 and y < 0:
        if x > -100 and x < 0:
            m_p_way.who_turn(-100,0,3)
        elif x > 0 and x < 100:
            m_p_way.who_turn(0,0,4)
        elif x > 100 and x < 200:
            m_p_way.who_turn(100,0,5)
       
    # створення третього рядка
    elif y > -200 and y < -100:
        if x > -100 and x < 0:
            m_p_way.who_turn(-100,-100,6)
        elif x > 0 and x < 100:
            m_p_way.who_turn(0,-100,7)
        elif x > 100 and x < 200:
            m_p_way.who_turn(100,-100,8)

def click_restart(x,y):
    if y < -85 and y > -120:
        if x > -25 and x < 150:

            m_d_b.finish[0] = True

            for i in range(9):
                m_d_b.komirka[i] = 0
            m_clear.clean()
