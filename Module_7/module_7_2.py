'''
https://urban-university.ru/members/courses/course999421818026/20231116-0000domasnee-zadanie-po-teme-pozicionirovanie-v-fajle-941056540023
2023/11/16 00:00|Домашнее задание по теме "Позиционирование в файле".
Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.
'''
file_seek=[]
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
file_name = 'temp7-2.txt'

def custom_write(file_name, strings:list, file_seek:list):
    file = open (file_name, 'w',encoding='utf-8')
    for i in strings:
        file_seek.append(file.tell())
        file.writelines(f'{i}\n')
    file.close()


def my_dict(file_name:str, file_seek:list):
    file = open(file_name, 'r', encoding='utf-8')
    x=1
    result=[]

    for i in (file.readlines()):
        result.append({(x, file_seek[x-1]):i})
        x+=1
    file.close()
    return result

custom_write(file_name, strings, file_seek)
print(my_dict(file_name, file_seek))