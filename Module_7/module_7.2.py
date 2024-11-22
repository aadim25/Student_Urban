'''
https://urban-university.ru/members/courses/course999421818026/20231116-0000domasnee-zadanie-po-teme-pozicionirovanie-v-fajle-941056540023
2023/11/16 00:00|Домашнее задание по теме "Позиционирование в файле".
Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.
'''
strings = ['111','223','333']
file_name = 'temp7-2.txt'
file_seek=[int]
def custom_write(file_name, strings:list):
    file = open (file_name, 'w')
    for i in strings:
        file_seek.append(file.tell())
        file.writelines(f'{i}\n')
    file.close()
    
def my_dict(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    x=1
    n=1
    text=''
    result=[{(int,int):str}]
    print (file_seek[0])
    # print(result)
    my_bool = True
    file.seek(0)
    while my_bool:
        if (file.readline()) !="":
            text = (file.readline())
            print(text)
            # z=file_seek[x]
            # file.seek(file_seek[0])
            result.append({(x, n): text})
            print('n ',n,'txt ',text, 'x ',x)
            x += 1
        else:
            my_bool=False
    print(result)
        #print(file.tell())
        #print(file.readline)
    print(result)
    file.close()

custom_write(file_name, strings)
my_dict(file_name)
#strings_positions
