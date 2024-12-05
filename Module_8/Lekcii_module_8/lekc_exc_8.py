# Пример один
# def greet_person(person_name):
#     if person_name=='Волан де Морт':
#         raise Exception('Мы не любим тебя, Волан де Морт')
#     print (f'Привет, {person_name}')
#
# greet_person('Джон')
# greet_person('Волан де Морт')

# Пример 2
# try:
#     raise NameError ('Привет, Там')
# except NameError as exc:
#     print (f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
#     raise

# class ProZero(Exception):
#     pass
#
# def f(a,b):
#     if b ==0:
#         raise ProZero('Деление на ноль невозможно')
#     return a/b
# print (f(3,2))
# print (f(3,0))

class ProZero(Exception):
    def __init__(self,message,extra_info):
        self.message = message
        self.extra_info = extra_info

def f(a,b):
    if b ==0:
        raise ProZero('Деление на ноль невозможно',{'a':a,'b':b})
    return a/b

try:
    result = f(10,0)
except ProZero as e:
    print ('Сегодня не очень хороший день, мы словили ошибку')
    print (f'Сообщение об ошибке {e.message}')
    print (f'Дополнительная информация: {e.extra_info}')
