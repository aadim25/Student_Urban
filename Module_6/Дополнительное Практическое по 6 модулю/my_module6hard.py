import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.filled = False
        self.__color = color
        self.__sides = sides if len(sides) == self.sides_count else [1]*self.sides_count
    def set_sides(self, *sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides

    def __is_valid_color(self,R,G,B):
        check_color = []
        if 0<=R<=255 and isinstance(R,int): check_color.append(True)
        else:
            check_color.append(False)
        if 0 <= G <= 255 and isinstance(R, int): check_color.append(True)
        else:
            check_color.append(False)
        if 0 <= B <= 255 and isinstance(R, int): check_color.append(True)
        else:
            check_color.append(False)
        if all(check_color):
            return True

    def set_color(self,R,G,B):
        if self.__is_valid_color(R,G,B):
            self.__color = (R, G, B)

    def get_color(self):
        return (self.__color)

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_sides(self, *sides):
        check = []
        for i in sides:
            if isinstance(i, int) and i > 0:
                check.append(i)
        if len(check) == self.sides_count:
            return True
        else:
            return False

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(self, sides, color)
        self.__radius = sides/(2*math.pi)

    def __len__(self, sides):
        return (sides)

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        (a, b, c) = self.get_sides()
        p = (a + b + c)/2
        self.height = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a if a > 0 else 0
    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.height
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__(color, [side] * 12)
        self.__sides = [side] * self.sides_count
    def get_volume(self):
        return self.get_sides()[0] ** 3





circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


'''
from math import pi
class Figure:
    sides_count = 0
    def __init__(self, *sides, *color, my_bool=False):
        self.__sides = sides if len(sides)==sides_count else [1]*self.sides_count
        self.__color = color
        self.filled = my_bool

    def get_sides(self):
        return (self.__sides)
    def get_color(self):
        return (self.__color)

    def set_color(self,R,G,B):
        if __is_valid_color(R,G,B):
            self.__color = (R, G, B)

    def set_sides(self, *sides):
        if len(sides) == len(self.__sides):
            valid_sides =[]
            for side in sides:
                if __is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides

    def __len__(self):
        sum_sides = 0
        for i in (self.__sides):
            sum_sides +=i
        return sum_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, cir):
        super().__init__(self, sides,color)
        self.__radius = cir/(2*pi)

    def __len__(self, cir):
        return (cir)

    def get_square(self):
        return pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, *sides, color):
        super().__init__(sides, *color)
        (a, b, c) = self.get_sides()
        p = (a + b + c)/2
        self.height = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a if a > 0 else 0
    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.height

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__([side] * 12, *color)
        self.__sides = [side] * self.sides_count
    def get_volume(self):
        return self.get_sides()[0] ** 3

figure=Figure(3,4,5)
#
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# # cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# # print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# Проверка объёма (куба):
# print(cube1.get_volume())


Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Наследование классов."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д. Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
'''