import customtkinter
import json
import modules.data_base as m_d_b
import modules.save_game as m_s_game

# Основна функція яка запускає гру
def start_game():
    import turtle
    import modules.create_screen as m_c_screen
    import modules.draw_table as m_d_table
    import modules.cell_click_detection as m_c_click

    m_d_table.draw_table(-100,100)
    m_c_screen.screen.onclick(m_c_click.click_cell, btn=1, add=True)
    turtle.done()

def lets_go():
    # Створення другого вінка з вибором хрестиків чи нуликів
    screen_c_z = customtkinter.CTk()
    app_c_z_width, app_c_z_height = 400, 200
    pc_screen_width = screen_c_z.winfo_screenwidth()
    pc_screen_height = screen_c_z.winfo_screenheight()
    screen_c_z.geometry(f"{app_c_z_width}x{app_c_z_height}+{pc_screen_width // 2 - app_c_z_width // 2}+{pc_screen_height // 2 - app_c_z_height // 2}")
    screen_c_z.resizable(False, False)
    screen_c_z.title("Cross/Zero")

    # отримання інформації з json
    with open(m_s_game.path, "r") as file:
        player1 = json.load(file)


    # Створення заголовку
    label_1 = customtkinter.CTkLabel(master = screen_c_z,
                                     text = f"Гравець '{player1['player_1']}' оберає за кого грати",
                                     font = ("Comic Sans MS", 20))
    label_1.pack(pady = 10)

    # Створення функції під кнопку "хрестики"
    def button_cross():
        m_d_b.step[0] = "cross"
        screen_c_z.destroy()
        start_game()
        

    # Створення функції під кнопку "нулики"
    def button_zero():
        m_d_b.step[0] = "zero"
        screen_c_z.destroy()
        start_game()
        

    # Створення кнопки хрестики
    btn_cross = customtkinter.CTkButton(master = screen_c_z,
                                        text = "ХРЕСТИКИ",
                                        font = ("Comic Sans MS", 17),
                                        width = 250,
                                        height = 35,
                                        fg_color = "tomato",
                                        command = button_cross)
    btn_cross.pack(pady = 10)

    # Створення кнопки нулики
    btn_zero = customtkinter.CTkButton(master = screen_c_z,
                                        text = "НУЛИКИ",
                                        font = ("Comic Sans MS", 17),
                                        width = 250,
                                        height = 35,
                                        fg_color = "dodgerblue",
                                        command = button_zero)
    btn_zero.pack(pady = 5)


    screen_c_z.mainloop()

