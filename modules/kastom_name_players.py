import customtkinter
import json
import modules.save_game as m_s_game
import modules.data_base as m_d_b
import modules.kustom_cross_or_zero as m_k_cz
from PIL import Image

# Створення першого вікна з іменнами гравців
screen_ctk = customtkinter.CTk()
app_width, app_height = 400, 300
pc_screen_width = screen_ctk.winfo_screenwidth()
pc_screen_height = screen_ctk.winfo_screenheight()
screen_ctk.geometry(f"{app_width}x{app_height}+{pc_screen_width // 2 - app_width // 2}+{pc_screen_height // 2 - app_height // 2}")
screen_ctk.resizable(False, False)
screen_ctk.title("Імена гравців")

# створення обєкта під малюнок
image_cross_zero = customtkinter.CTkImage(light_image = Image.open(m_s_game.path_to_file('image\\1.jpg')),
                                          dark_image = Image.open(m_s_game.path_to_file('image\\1.jpg')),
                                          size = (100, 100))
image_label = customtkinter.CTkLabel(master = screen_ctk,
                                     image = image_cross_zero,
                                     text='')
image_label.pack(pady = 20)

# створення стилю під введення
style = ("Comic Sans MS", 15)

# Поля під введення гравців
input_player_1 = customtkinter.CTkEntry(master = screen_ctk, 
                                        placeholder_text = "Введіть ім'я першого гравця", 
                                        width = 300,
                                        height = 30,
                                        font = style,
                                        border_color = "mediumpurple")
input_player_1.place(x = app_width // 2, y = app_height // 2, anchor = customtkinter.CENTER)

input_player_2 = customtkinter.CTkEntry(master = screen_ctk, 
                                        placeholder_text = "Введіть ім'я другого гравця", 
                                        width = 300,
                                        height = 30,
                                        font = style,
                                        border_color = "mediumpurple")
input_player_2.place(x = app_width // 2, y = app_height // 2 + 50, anchor = customtkinter.CENTER)

#створення тексту під помилку про введення двох гравців
text_input = """Ой! 
Ти забув вказати 2-ох гравців!"""
# створення тексту під помилку про повторення імен
text_repetition = """Oops!
Імена не можуть повторюватись!"""

# створення функції, яка відповідає за вікно помилки про обовязкове введення гравців
def must_input_names(text_eror = text_input):
    # вікно помилки
    screen_error_1 = customtkinter.CTk()
    error_1_width, error_1_height = 350, 150
    screen_error_1.geometry((f"{error_1_width}x{error_1_height}+{pc_screen_width // 2 - error_1_width // 2}+{pc_screen_height // 2 - error_1_height // 2}"))
    screen_error_1.resizable(False,False)
    screen_error_1.title("Ooops")
    # текст помилки
    label_error_1 = customtkinter.CTkLabel(master = screen_error_1,
                                            text = text_eror,
                                            font = ("Comic Sans MS", 20))
    label_error_1.place(x = error_1_width // 2, y = error_1_height // 2 - 30, anchor = customtkinter.CENTER)
    # функція під кнопку ок
    def close_error_1():
        screen_error_1.destroy()
    # кнопка ок 
    btn_error_1 = customtkinter.CTkButton(master = screen_error_1,
                                          text = "OK",
                                          fg_color = "slateblue",
                                          border_color = "white",
                                          border_width = 2,
                                          font = ("Comic Sans MS", 15),
                                          command = close_error_1) 
    btn_error_1.place(x = error_1_width // 2, y = error_1_height // 2 + 30, anchor = customtkinter.CENTER)
    screen_error_1.mainloop()

# створення функції, яка відповідає за вікно помилки про повторення імен
def dont_repetition_names():
    must_input_names(text_eror = text_repetition)
    
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

# створення функції під кнопку "ГОТОВО"
def comand_button():
    dict_players["player_1"]["name"] = input_player_1.get()
    dict_players["player_2"]["name"] = input_player_2.get()

    with open (m_s_game.path, "w") as file:
        json.dump(dict_players, file, ensure_ascii = False, indent = 4)

    if dict_players["player_1"]["name"] == '' or dict_players["player_2"]["name"] == '':
        must_input_names()

    elif dict_players["player_1"]["name"] == dict_players["player_2"]["name"]:
        dont_repetition_names()
    
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
button.place(x = app_width // 2, y = app_height // 2 + 100, anchor = customtkinter.CENTER)

screen_ctk.mainloop()