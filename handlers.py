import os
from pathlib import Path

def create_folder(path):
    create_f = False
    while not create_f:
        name = input("Введите наименование папки (для отмены - cancel): ")
        if name == "cancel":
            return True
        if not os.path.isdir(Path(path) / name):
            os.mkdir(Path(path) / name)
            print(f"Папка {name} создана!")
            create_f = True
            return True
        else:
            print("Папка с таким именем уже существует! Попробуйте еще раз!")


def delete_folder():
    delete_f = False
    while not delete_f:
        name = input("Введите наименование папки (для отмены - cancel): ")
        if name == "cancel":
            return True
        if os.path.isdir(name):
            os.removedirs(name)
            print(f"Папка {name} удалена!")
            delete_f = True
            return True
        else:
            print("Папка с таким именем не существует! Попробуйте еще раз!")


def create_file():
    create_f = False
    while not create_f:
        name = input("Введите наименование файла (для отмены - cancel): ")
        if name == "cancel":
            return True
        if (not os.path.exists(name)) and (not os.path.isfile(name)):
            text_file = open(name, "w")
            text_file.close()
            print(f"Файл {name} создан!")
            create_f = True
            return True
        else:
            print("Файл с таким именем уже существует! Попробуйте еще раз!")

def write_to_file():
    create_f = False
    while not create_f:
        name = input("Введите наименование файла (для отмены - cancel): ")
        if name == "cancel":
            return True
        if (os.path.exists(name)) and (os.path.isfile(name)):
            text_file = open(name, "a")
            text = input("Введите текст, который нужно записать в файл (последнее слово - stop, для отмены - cancel):\n")
            if text == "cancel":
                return True
            text_array = [text]
            while text != 'stop':
                text = input()
                text_array.append(text)
            text_array = [line+'\n' for line in text_array][:-1]
            text_file.writelines(text_array)
            text_file.close()
            print(f"Запись текста в файл {name} успешно осуществлена!")
            create_f = True
            return True

        else:
            print("Файл с таким именем не существует! Попробуйте еще раз!")

def open_file():
    open_f = False
    while not open_f:
        name = input("Введите наименование файла (для отмены - cancel): ")
        if name == "cancel":
            return True
        if (os.path.exists(name)) and (os.path.isfile(name)):
            text_file = open(name, "r")
            print('Cодержимоe текстового файла\n', text_file.read())
            text_file.close()
            open_f = True
            return True

        else:
            print("Файл с таким именем не существует! Попробуйте еще раз!")

def delete_file():
    delete_f = False
    while not delete_f:
        name = input("Введите наименование файла (для отмены - cancel): ")
        if name == "cancel":
            return True
        if (os.path.exists(name)) and (os.path.isfile(name)):
            os.remove(name)
            print(f"Файл {name} удален!")
            delete_f = True
            return True

        else:
            print("Файл с таким именем не существует! Попробуйте еще раз!")

