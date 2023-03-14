import modules.draw_cross as m_d_cross
import modules.draw_zero as m_d_zero
import modules.data_base as m_d_b
import modules.win_lose as m_w_l
import modules.clear as m_clear
import modules.save_game as m_s_game
import modules.table_result as m_t_result
import json
import turtle



def who_turn(x, y, index):
    if m_d_b.step[0] == "cross" and m_d_b.komirka[index] == 0 and m_d_b.finish[0]:
        m_d_cross.draw_cross(x, y)
        m_d_b.step[0] = "zero"
        m_d_b.komirka[index] = 1

        m_w_l.horizontal_victory(1, -50, 50, 0, 3)
        m_w_l.horizontal_victory(1, -50, -50, 3, 6)
        m_w_l.horizontal_victory(1, -50, -150, 6, 9)

        m_w_l.vertical_victory(0, 1, -50, 50)
        m_w_l.vertical_victory(1, 1, 50, 50)
        m_w_l.vertical_victory(2, 1, 150, 50)

        m_w_l.diagonal_victory(1)


        if m_d_b.finish[0] == False:

            with open(m_s_game.path, 'r') as file:
               players = json.load(file)

            players["player_1"]["count_win"] += 1

            # print(players["player_1"]["count_win"])
            # m_t_result.count_win(-320,100)

            with open(m_s_game.path, 'w') as file:
                json.dump(players, file, ensure_ascii = False, indent = 4)

            m_t_result.count_win()
                
    elif m_d_b.step[0] == "zero" and m_d_b.komirka[index] == 0 and m_d_b.finish[0]:
        m_d_zero.draw_zero(x, y)
        m_d_b.step[0] = "cross"
        m_d_b.komirka[index] = 2

        m_w_l.horizontal_victory(2,-50, 50, 0, 3)
        m_w_l.horizontal_victory(2,-50, -50, 3, 6)
        m_w_l.horizontal_victory(2,-50, -150, 6, 9)

        m_w_l.vertical_victory(0,2, -50,50)
        m_w_l.vertical_victory(1,2, 50,50)
        m_w_l.vertical_victory(2,2, 150,50)

        m_w_l.diagonal_victory(2)

        if m_d_b.finish[0] == False:

            with open(m_s_game.path, 'r') as file:
               players = json.load(file)
            
            players["player_2"]["count_win"] +=1

            # print(players["player_2"]["count_win"])
            # m_t_result.count_win(-320,100)

            with open(m_s_game.path, 'w') as file:
                json.dump(players, file, ensure_ascii = False, indent = 4)

            m_t_result.count_win()
            
    
