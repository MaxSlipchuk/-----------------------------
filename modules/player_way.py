import modules.draw_cross as m_d_cross
import modules.draw_zero as m_d_zero
import modules.data_base as m_d_b
import modules.win_lose as m_w_l
import modules.clear as m_clear
import modules.save_game as m_s_game
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
            
            # win_1 = 0

            # with open(m_s_game.path, 'r') as file:
            #    players = json.load(file)

            # count_winner_1 = 'кількість перемог: '+ str(win_1 + 1)
            # players["player_1"] += count_winner_1

            # with open(m_s_game.path, 'w') as file:
            #     json.dump(count_winner_1, file, ensure_ascii = False, indent = 4)


            restart = turtle.textinput("Restar", """Почати гру спочатку?
        Напишіть 'так'""")
        
            if restart == 'так':
                m_d_b.finish[0] = True

                for i in range(9):
                    m_d_b.komirka[i] = 0

                m_clear.clean()

            elif restart == 'ні':
                print("Тоді щасти!")
                

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

            # win_2 = 0

            # with open(m_s_game.path, 'r') as file:
            #    players = json.load(file)
            
            # count_winner_2 = "кількісьть перемог: " + str(win_2 + 1)
            # players["player_2"] += count_winner_2

            # with open(m_s_game.path, 'w') as file:
            #     json.dump(count_winner_2, file, ensure_ascii = False, indent = 4)

            restart = turtle.textinput("Restar", """Почати гру спочатку?
        Напишіть 'так'""")
        
            if restart == 'так':
                m_d_b.finish[0] = True

                for i in range(9):
                    m_d_b.komirka[i] = 0

                m_clear.clean()

            elif restart == 'ні':
                print("Тоді щасти!")
        
    
