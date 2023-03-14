import os
import json

def path_to_file(name_file):
    path_file = __file__.split("\\")
    del path_file[-1]
    del path_file[-1]
    path_file = '\\'.join(path_file)
    # зберігаємо в змінну шлях до файлу + імя файла яке хочемо зберегти, модуль ос правильно його обєднує
    path_file = os.path.join(path_file, name_file)
    return path_file

path = path_to_file("json\\json_new.json")
