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
'''
import os
my_root = []
my_dir = []
my_file = []
print (os.getcwd())
os.chdir('H:') # Изображения
# print (os.listdir('.'))
# for i in os.listdir('.'):

for roots, dirs, files in os.walk('H:'):
    # print(dirs)
    my_root.append(roots)
    my_dir.append(dirs)
    my_file.append(files)

# filepath =

# print (os.path.basename('.'))
for i in my_root:
    print (os.path.split(i))
    print ('Roots ',i)
    for j in os.listdir(i):
        # print (os.path.split(my_root))
        print('Files ', (j))

# for j in my_dir:
#     print (os.path.split(j))
#     print ('Dirs ',j)



