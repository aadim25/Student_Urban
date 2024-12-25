'''
Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

'''

def is_prime(function):
    def wrapper(*args):
        count = 0
        func = function(*args)
        for i in range(2,func+1):
            if func%i==0:
                count+=1
            if count>=2:
                return  f'Сложное'
        if count == 1:
            return f'Простое'
    return wrapper

@is_prime
def sum_three(*args):
    my_sum=0
    for i in args:
        my_sum+=i
    return my_sum

result = sum_three(2, 3, 6)
print(result)

'''Черновик
'''