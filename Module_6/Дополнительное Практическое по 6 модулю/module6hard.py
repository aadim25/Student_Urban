import math
class Figure:
    sides_count = 0

    # инициализация класса Figure
    def __init__(self, color:tuple[int,int,int], *sides, filled):
        self.filled = filled
        self.__color = color
        self.__sides = sides

    def get_color(self):
        # Получение цвета
        return self.__color

    def __is_valid_color(self,R,G,B): # функция проверки цветов
        valid_value = 0<=R<=255 and 0<=G<=255 and 0<=B<=255
        valid_type = isinstance(R,int) and isinstance(G,int) and isinstance(B,int)
        return valid_value and valid_type

    def set_color(self, R, G, B):
        # Установка цвета
        if self.__is_valid_color(R, G, B):
            self.__color = (R, G, B)

    def __is_valid_sides (self, *sides): # функция проверки сторон
        for side in sides:
            if not isinstance(side,int) or side<0:
                return False
        return True

    def get_sides(self):
        # Получение стороны
        return self.__sides

    def __len__(self):
        # Получение параметров длины
        return sum(self.__sides)

    def set_sides(self, *new_sides): # Функция установки значений сторон
        if len(new_sides) == len(self.__sides):
            valid_sides = [] # Переменная для внутреннего цикла
            for side in new_sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides


class Circle(Figure):
    sides_count = 1 # число сторон, т.е. длина окружности

    def __init__(self, color:tuple[int,int,int], length, filled = False):
        # Новая окружность
        super().__init__(color, length, filled = filled) # обращение к родительскому классу
        self.__radius = length/(2*math.pi) # вычисление радиуа


    def get_square(self):
        # Вычисление площади окружности
        return len(self)**2 / (4*math.pi)
class Triangle(Figure):
    sides_count = 3 # Число сторон
    def __init__(self, color:tuple[int,int,int], heigth, *sides, filled = False): # Инициализация
        super().__init__(color, *sides, filled=filled) # Передача в родительский класс

    def get_square(self):
        p = (len(self))/2 # вычиление периметра
        sides = self.get_sides() # получение длин сторон
        return math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2])) # Площадь

class Cube(Figure):
    sides_count = 12
    def __init__(self, color:tuple[int,int,int], side,filled=False): # Инициализация нового куба
        cube_sides = [side] * 12 # длина сторон
        super().__init__(color, cube_sides, filled=filled) # передача в фигуру

    def get_volume(self):
        # Вычисление объема куба
        return self.get_sides()[0][0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) #'Окружность, get_color',
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color()) #'Куб, get_color',

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # 'get_sides_cube',
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
