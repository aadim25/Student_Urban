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

def add_everything_up(a,b):

    try:
        i = a + b
    except TypeError as exc:
        print("Нельзя складывать пременные разных типов", exc)
        if type(a)==str and type(b)!=str:
            i = a+str(b)
        elif type(b)==str and type(a)!=str:
            i = b +str(a)
        else:
            i = b + a
    else:
        print("Сложение выполняется", i)
    finally:
        print("Файнали, мы заканчиваем урок")

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('тыква', 'подсолнух'))