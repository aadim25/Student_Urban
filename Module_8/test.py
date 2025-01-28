# try:
#     file=open('blabla.txt')
    # a=10/0
    # truba = a+b
    # trube = 10/0
    # i=0
    # print(10/i)
    # print ("Сделано")
# except OSError as exc:
#     print(f'Вот что пошло не так - {exc} параметры {exc.args} но мы еще на плаву')
# except ZeroDivisionError as exc:
#     print(f'Вот что пошло не так - {exc}, но мы еще на плаву')
# except ZeroDivisionError as exc:
    # print ('Они - убили Кенни - хотели делить на ноль, но мы не упали')
    # print(f'Вот что пошло не так - {exc}, но мы еще на плаву')
# except NameError:
#     print ("Нет такой переменной, кто писал этот код?")

print ("Какой хороший день, предлагаю научиться работать с исключениями")
i = int(input('Введите число: '))
try:
    result = 10 * (1 / i)
except ZeroDivisionError as exc:
    print ("Нельзя делить на ноль,", exc)
else:
    print ("ура, мы не будем делить на ноль")
finally:
    print ("Файнали, мы заканчиваем урок")