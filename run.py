import os
from settings import *
from handlers import *

def menu(path):
    correct_num = False
    while not correct_num:
        try:
            print(f"Рабочая директория {path}, текущая директория - {os.getcwd()}\n"
                "Выберите пункт меню:\n \
            1. Создание папки (с указанием имени);\n \
            2. Удаление папки по имени;\n \
            3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх; \n \
            4. Создание пустых файлов с указанием имени;\n \
            5. Запись текста в файл;\n \
            6. Просмотр содержимого текстового файла; \n \
            7. Удаление файлов по имени;\n \
            8. Копирование файлов из одной папки в другую; \n \
            9. Перемещение файлов; \n \
            10. Переименование файлов;\n \
            11. Изменить расположение рабочей папки.\n "
            )
            menu_num = input()
            if menu_num == 'exit':
                return 'exit'
            else:
                menu_num = int(menu_num)
            correct_num = True
            if (menu_num < 1) or (menu_num > 11):
                raise ValueError
        except ValueError:
            print("Введено некорректное значение! Попробуйте еще раз!")
            correct_num = False
    return menu_num


curr_dir = set_dir()
print("Текущая директория изменилась на:", os.getcwd())
menu_num = 0
ch = "/Users/a19078663/Downloads"
#/Users/a19078663/Downloads
while menu_num != 'exit':
    menu_num = menu(curr_dir.path)
    if menu_num == 1:
        create_folder(curr_dir.path)
    elif menu_num == 2:
        delete_folder()
    elif menu_num == 3:
        delete_folder()#not ready
    elif menu_num == 4:
        create_file()
    elif menu_num == 5:
        write_to_file()
    elif menu_num == 6:
        open_file()
    elif menu_num == 7:
        delete_file()
    elif menu_num == 8:
        write_to_file()
    elif menu_num == 9:
        write_to_file()
    elif menu_num == 10:
        write_to_file()
    elif menu_num == 11:
        os.chdir('test')
