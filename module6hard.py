from math import pi, sqrt


class Figure:
    # Атрибуты класса Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    # возвращает список RGB цветов
    def get_color(self):
        return self.__color

    # Метод __is_valid_color - служебный, принимает параметры r, g, b, проверяет корректность переданных значений
    # перед установкой нового цвета. Корректный цвет: все значения r, g и b - целые числа от 0 до 255 (вкл.).
    def __is_valid_color(self, r, g, b):
        if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return False
        elif not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False
        return True

    # Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
    # целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *sides): #((20, 10),)
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return True

    # Метод get_sides должен возвращать значение я атрибута __sides.
    def get_sides(self):
        return self.__sides

    # Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)

    # Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    # то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides): # (20, 10)
            self.__sides = new_sides


# Каждый объект класса Circle должен обладать всеми атрибутами и методами класса Figure. Атрибут __radius,
# рассчитать исходя из длины окружности (одной единственной стороны).
class Circle(Figure):
    # Атрибуты класса Circle:
    sides_count = 1
    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            new_sides = [1]
        super().__init__(color, *sides)
        self.__radius = len(self) / (2 * pi)

    # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    def get_square(self):
        return pi * self.__radius ** 2

    def set_sides(self, *new_sides): # new_sides = (10, 15). Len = 2
        if len(new_sides) != self.sides_count:
            new_sides = [1]
        super().set_sides(*new_sides) # изменилась сторона
        self.__radius = self.__radius = len(self) / (2 * pi)


# Каждый объект класса Triangle должен обладать всеми атрибутами и методами класса Figure
class Triangle(Figure):
    # Атрибуты класса Triangle:
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
    def get_square(self):
        s = sum(self.__sides) / 2
        return sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))


# Каждый объект класса Cube должен обладать всеми атрибутами и методами класса Figure
class Cube(Figure):
    # Атрибуты класса Cube:
    sides_count = 12

    def __init__(self, color, *sides): # (10,)
        if len(sides) != 1:
            sides = [1]
        self.sides = sides * self.sides_count # сборка
        super().__init__(color, *sides)

    # Метод get_volume, возвращает объём куба.
    def get_volume(self):
        return self.sides[0] ** 3



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