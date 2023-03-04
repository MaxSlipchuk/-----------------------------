import modules.data_base as m_d_b
from tkinter import*
from tkinter import ttk
import modules.save_game as m_s_game
import json



def start_game():
    import turtle
    import modules.create_screen as m_c_screen
    import modules.draw_table as m_d_table
    import modules.cell_click_detection as m_c_click

    m_d_table.draw_table(-100,100)
    m_c_screen.screen.onclick(m_c_click.click_cell, btn=1, add=True)
    turtle.done()


def root_choice():
    # створення головного вікна
    root = Tk()
    root.title("Зіграємо?")
    # розмір і координати
    root.geometry('300x220+500+200')
    # відключення зміни параметрів висоти і ширини
    root.resizable(False, False)

    # створення мітки на вікні
    label = Label(text = '''ПРИВІТ!''', font = ("Sylfaen", 20))
    # виведення мітки у вікні
    label.pack()

    # створення поля для ведення імені гравця
    text_1 = StringVar()
    player_1 = ttk.Entry( width=30, textvariable = text_1)
    player_1.pack(pady=3)
    
    text_2 = StringVar()
    player_2 = ttk.Entry(width=30,textvariable = text_2)
    player_2.pack()

    # створення функції під кнопку хрестики
    def btn_cross_fun ():
        m_d_b.step[0] = 'cross'
        print(player_1.get())

        dict_2 = {
            "player_1": player_1.get(),
            "player_2": player_2.get()
        }

        with open(m_s_game.path, 'w') as file:
            json.dump(dict_2, file, ensure_ascii = False, indent = 4)

        root.destroy()
        # start_game()
    

    label_2 = Label(text = '''Перший гравець оберає
    за кого грати. ''', font = ("Sylfaen", 15))
    label_2.pack(pady = 5)

    # створення кнопки "ХРЕСТИКИ"
    btn_cross = ttk.Button(text = "ХРЕСТИКИ", width = 30,command = btn_cross_fun)
    btn_cross.pack()

    # створення функції під нулики
    def btn_zero_fun():
        m_d_b.step[0] = 'zero'
        print(text_2.get())
        root.destroy()
        start_game()
        

    # створення кнопки "НУЛИКИ"
    btn_zero = ttk.Button(text = "НУЛИКИ", width = 30, command = btn_zero_fun)
    btn_zero.pack()
    root.mainloop()

root_choice()
