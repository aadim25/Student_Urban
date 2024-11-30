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
'''import os
my_dir = []
my_file = []
# my_dir = os.getcwd()
my_lst = os.walk('.')
for root, dirs,files in my_lst:

    for dir in dirs:
        my_dir.append(dir)

    for file in files:
        my_file.append(file)

# print(os.listdir('.'))
for dir in my_dir:
    print (dir)
# print (my_file)'''
import os
my_dir = []
my_file = []
my_root = []
print(os.getcwd())
os.chdir('H:\Изображения')
print('getcwd',os.getcwd())
#print(os.getcwd())
#my_lst = os.walk('.')
#print(my_lst)
for roots, dirs, files in os.walk('.'):
    for root in roots:
        my_root.append(root)

    for dir in dirs:
        my_dir.append(dir)
        #print(dir)

    for file in files:
        #print(file)
        my_file.append(file)

for root in my_root:
    print(root)

    print(os.listdir(os.chdir(root)))

for root in my_root:
    print (root)
for dir in my_dir:
    print (dir)
    # my_str = 'H:\Изображения'
    # os.chdir(dir)
    for my_path,sec_dir,sec_files in os.walk(dir):
        for file in sec_files:
            print (file)