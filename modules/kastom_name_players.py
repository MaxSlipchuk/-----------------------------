import customtkinter
import json
import modules.save_game as m_s_game
import modules.data_base as m_d_b
import modules.kustom_cross_or_zero as m_k_cz



# Створення першого вікна з іменнами гравців
screen_ctk = customtkinter.CTk()
app_width, app_height = 400, 200
pc_screen_width = screen_ctk.winfo_screenwidth()
pc_screen_height = screen_ctk.winfo_screenheight()
screen_ctk.geometry(f"{app_width}x{app_height}+{pc_screen_width // 2 - app_width // 2}+{pc_screen_height // 2 - app_height // 2}")
screen_ctk.resizable(False, False)
screen_ctk.title("Імена гравців")

# створення стилю під введення
style = ("Comic Sans MS", 15)

# Поля під введення гравців
input_player_1 = customtkinter.CTkEntry(master = screen_ctk, 
                                        placeholder_text = "Введіть ім'я першого гравця", 
                                        width = 300,
                                        height = 30,
                                        font = style,
                                        border_color = "mediumpurple")
input_player_1.place(x = app_width // 2, y = app_height // 2 - 40, anchor = customtkinter.CENTER)

input_player_2 = customtkinter.CTkEntry(master = screen_ctk, 
                                        placeholder_text = "Введіть ім'я другого гравця", 
                                        width = 300,
                                        height = 30,
                                        font = style,
                                        border_color = "mediumpurple")
input_player_2.place(x = app_width // 2, y = app_height // 2, anchor = customtkinter.CENTER)

# створення функції під кнопку "ГОТОВО"

dict_players = {
    "player_1": {
                    "name": '',
                    "count_win": 0
                },
    "player_2": {
                    "name": '',
                    "count_win": 0
                }
}

def comand_button():
    
    dict_players["player_1"]["name"] = input_player_1.get()
    dict_players["player_2"]["name"] = input_player_2.get()

    with open (m_s_game.path, "w") as file:
        json.dump(dict_players, file, ensure_ascii = False, indent = 4)

    if dict_players["player_1"] != '' and dict_players["player_2"] != '':
        screen_ctk.destroy()
        m_k_cz.lets_go()
        

# Створення кнопки "ГОТОВО"
button = customtkinter.CTkButton(master = screen_ctk,
                                 text = "ГОТОВО",
                                 fg_color = "slateblue",
                                 border_color = "white",
                                 border_width = 2,
                                 font = ("Comic Sans MS", 15),
                                 command = comand_button)
button.place(x = app_width // 2, y = app_height // 2 + 50, anchor = customtkinter.CENTER)

screen_ctk.mainloop()