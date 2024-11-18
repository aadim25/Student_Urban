'''Файл после корректировки Юрия'''
import math
class Figure:
    sides_count = 0
    def __init__(self, color:tuple[int,int,int], *sides, filled = False):
        # print ('Новая фигура', color, sides)
        # sides = [6,6,6,6,6,6,6,6,6,6,6,6]
        # print ('Значение color', (color))
        # print ('sides перед self', sides, type(sides))
        # print ('Длина sides', len(sides))
        self.filled = filled
        self.__color = color
        # self.__sides = sides if len(sides)==self.sides_count else [1]*self.sides_count
        self.__sides = sides
        # print('Проверка на кортеж self.__sides', self.__sides, type(self.__sides))

    def get_color(self):
        # print('Получение цвета')
        return self.__color

    def __is_valid_color(self,R,G,B):
        valid_value = 0<=R<=255 and 0<=G<=255 and 0<=B<=255
        valid_type = isinstance(R,int) and isinstance(G,int) and isinstance(B,int)
        return valid_value and valid_type

    def set_color(self, R, G, B):
        # print ('Установка цвета')
        if self.__is_valid_color(R, G, B):
            self.__color = (R, G, B)

    def __is_valid_sides (self, *sides):
        for side in sides:
            if not isinstance(side,int) or side<0:
                return False
        return True

    def get_sides(self):
        # print('Получение стороны', self.__sides)
        return self.__sides

    def __len__(self):
        # print('Получение периметра')
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            valid_sides = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color:tuple[int,int,int], length, filled = False):
        # print('Новая окружность')
        super().__init__(color, length, filled = filled)
        self.__radius = length/(2*math.pi)


    def get_square(self):
        # print('Вычисление площади окружности')
        return len(self)**2 / (4*math.pi)
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides, filled):
        super().__init__(color, sides)
        (a, b, c) = self.get_sides()
        p = (a + b + c)/2
        self.height = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a if a > 0 else 0
    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.height
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        # print('Новый куб, сторона', side)
        sides = [side] * 12
        print('Куб sides', type(sides))
        super().__init__(color, sides)

    def get_volume(self):
        print('Вычисление объема куба')
        return self._Figure__sides[0] ** 3


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