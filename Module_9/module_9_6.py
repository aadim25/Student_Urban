'''2023/12/04 00:00|Домашнее задание по теме "Генераторы"
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc

Примечания:
Для функции генератора используйте оператор yield.

Файл module_9_6.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!'''

def all_variants(text):
    for k in range(len(text)):
        for j in range(len(text)-k):
            #
            yield (text[j:j+k+1])

gener = all_variants('abc')
for k in gener:
    print (k)



'''черновик
 # print (f'i={i} j={j} (j+i+1)={j+i+1} text={text[-1:1]} len(text)={len(text)}')
 print(f'i={i} j={j} (j+i+1)={j + i + 1} text={text[j:i+j+1]}')
 '''