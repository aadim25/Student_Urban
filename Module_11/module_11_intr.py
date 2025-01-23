'''Домашнее задание по теме "Интроспекция"
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
'''
import inspect
import math
import requests
import sys
from collections import defaultdict
from pprint import pprint
def my_attr():
    pass
def introspection_info(obj):
    my_lst = defaultdict(list)

    for attr in dir(obj):
        get_attr = getattr(obj,attr)
        if inspect.isbuiltin(get_attr):
            my_lst['Встроенная функция или метод'].append(attr)
        if inspect.isfunction(get_attr):
            my_lst['Функция'].append(attr)
        if inspect.ismethod(get_attr):
            my_lst['Метод'].append(attr)
        if inspect.isclass(get_attr):
            my_lst['Класс'].append(attr)
        if inspect.ismodule(get_attr):
            my_lst['Модуль'].append(attr)
        if attr.startswith('_'):
            my_lst['Магические методы'].append(attr)
    return my_lst

number_info = introspection_info(42)
pprint(number_info)
number_info = introspection_info(inspect)
pprint(number_info)