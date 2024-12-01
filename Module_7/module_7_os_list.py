'''
Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:

Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
Пример возможного вывода:
Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.
'''
import os, datetime, time
my_root = []
my_dir = []
my_file = []
directory='.' # H:\Изображения
print (os.getcwd())
# os.chdir('H:') # Изображения
# print (os.listdir('.'))
# for i in os.listdir('.'):

for roots, dirs, files in os.walk(directory):
    filepath = roots

    print (filepath)
    # print ('dirs',dirs)
    for i in roots:
        if for a,b,c in os.walk(i):
        for j in files:
            if i =='.':
                my_str = str(j)
            else:
                my_str = str(i) + str(j)
            print (my_str)
            print (filepath)
            filetime = os.path.getmtime(my_str)
            print (filetime)

# for roots, dirs, files in os.walk('H:'):
#     # print(dirs)
#     my_root.append(roots)
#     my_dir.append(dirs)
#     my_file.append(files)





