'''
Задание "Программистам всё можно":
Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!

Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)

Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.

Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

Вывод в консоль:
123.456строка
яблоко4215
130.456
'''
import decimal
# getcontext().prec = 6
def add_everything_up(a,b):

    try:
        i = a + b
    except TypeError as exc:
        i = str(a) + str(b)
    finally:
        print (i)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



#------------- дальше идет черновик------------
# print(add_everything_up('тыква', 'подсолнух'))
# decimal(