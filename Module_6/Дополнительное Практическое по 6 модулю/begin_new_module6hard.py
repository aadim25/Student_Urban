import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        # print ('Новая фигура', color, sides)
        print ('Значение color', (color))
        print('sides перед self', sides)
        print ('Длина sides', len(list(sides)))
        self.filled = False
        self.__color = color
        self.__sides = list(sides) if len(sides) == self.sides_count else [1]*self.sides_count
        print('self.__sides', self.__sides)
    def set_sides(self, *new_sides):
        # print('Установка стороны', sides)
        # if len(new_sides) == self.sides_count:
        #     valid_sides = []
        #     for side in new_sides:
        #         if self.__is_valid_sides(side):
        #             print('side', side)
        #             valid_sides.append(side)
        #             print(valid_sides)
        #     self.__sides = valid_sides
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            print('new_sides', new_sides)

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
        # print ('Установка цвета')
        if self.__is_valid_color(R,G,B):
            self.__color = (R, G, B)

    def get_color(self):
        # print('Получение цвета')
        return self.__color

    def get_sides(self):
        # print('Получение стороны', self.__sides)
        return self.__sides

    def __len__(self):
        # print('Получение периметра')
        return sum(self.__sides)

    def __is_valid_sides(self, *sides):
        # print('Валидация')
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
        # print('Новая окружность')
        super().__init__(color, sides)
        self.__radius = sides/(2*math.pi)


    def get_square(self):
        # print('Вычисление площади окружности')
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
        print('Новый куб, сторона', side)
        sides = [side] * 12
        super().__init__(color, list(sides))

    def get_volume(self):
        # print('Вычисление объема куба')
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
print('get_sides_cube', cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
