import os


def set_dir():
    while True:
        path = input("Введите путь к рабочей папке: ")
        if os.path.isdir(path):
            os.chdir(path)
            print("Текущая директория изменилась на:", os.getcwd())
            return path
        else:
            print("Введены некорректные данные! Повторите попытку!")

