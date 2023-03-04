import os
import json

def path_to_file(name_file):
    path_file = __file__.split("\\")
    del path_file[-1]
    del path_file[-1]
    path_file = '\\'.join(path_file)
    path_file = os.path.join(path_file, name_file)
    return path_file

path = path_to_file("json_new.json")

# dict_1 = {
#     "name_1": "Max",
#     "name_2": "Oleg"
# }

# with open(path, 'w') as file:
#     json.dump(dict_1, file, ensure_ascii = False, indent = 4)


print(path)