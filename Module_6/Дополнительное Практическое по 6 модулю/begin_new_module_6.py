import math
class Figure:
    sides_count = 0
    def __init__(self, color: tuple[int,int,int], *sides, filled=False):
        #print ('Новая фигура', color, *sides)
        self.filled = filled
        self.__color = color
        self.__sides = sides
    
    def set_sides(self, *sides):
        #print('Установка стороны', sides)
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid_sides(side):
                    #print('side', side)
                    valid_sides.append(side)
            self.__sides = valid_sides

    def __is_valid_color(self,R,G,B):
        check_value = 0<=R<=255 and 0<=G<=255 and 0<=B<=255 
        check_type= isinstance(R,int) and isinstance(R,int) and isinstance(R,int)
        return check_value and check_type

    def set_color(self,R,G,B):
        #print ('Установка цвета')
        if self.__is_valid_color(R,G,B):
            self.__color = (R, G, B)

    def get_color(self):
       # print('Получение цвета')
        return (self.__color)

    def get_sides(self):
       # print('Получение стороны', self.__sides)
        return self.__sides

    def __len__(self):
        #print('Получение периметра')
        return sum(self.__sides)

    def __is_valid_sides(self, *sides):
        #print('Валидация')
        check = []
        for i in sides:
            if not isinstance(i, int) or i <0:
                return False
        return True
            

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length, filled=False):
      #  print('Новая окружность')
        super().__init__(self, color, length,filled=filled)
        self.__radius = length/(2*math.pi)

    def __len__(self, sides):  
        return (sides)


    def get_square(self):
       # print('Вычисление площади окружности')
        return len(self)**2/(4*math.pi)

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
       # print('Новый куб, сторона', side)
        super().__init__(color, [side] * self.sides_count)
        #self.__sides = [side] * self.sides_count
    def get_volume(self):
      #  print('Вычисление объема куба')
        return self.get_sides()[0] ** 3

    # def get_color(self):
    #     return self.__color


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) # 'Окружность, get_color'
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color()) #'Куб, get_color', 

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())