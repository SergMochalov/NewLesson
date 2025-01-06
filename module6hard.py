import math


class Figure:
    filled = False
    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color

    def get_color (self):
        return self.__color

    def set_color (self, r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = r,g,b
        else:
            print('Not correct color')
        return self.__color

    def __is_valid_color(self, r,g,b):

        if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:
            return True
        else:
            return False

    def get_sides (self):
        x = self.sides_count
        ss = []
        while x > 0:
            x -= 1
            ss.append(self.__sides)
        self.__sides = ss
        return self.__sides

    def set_sides (self, *new_sides):
        s = new_sides
        if self.__is_valid_sides(s):
            for i in range(len(s)):
                self.__sides = s[i]
            return self.__sides




    def __is_valid_sides(self,s):
        if self.sides_count == len(s):
            return True
        else:
            return False



    def __len__ (self):
        __radius = self.__sides[0] / 2
        print(__radius)
        _square =int ( math.pi * (__radius ** 2))
        return _square


    def __len__ (self):
        __radius = self.__sides[0] / 2
        _square =int ( math.pi * (__radius ** 2))
        return _square

    def get_volume(self):
        _square = self.__sides[0] ** 3
        return _square




class Circle(Figure):
    sides_count = 1

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        __pp = (self.__sides[0] + self.__sides[1] + self.__sides[2] )/ 2
        _square = math.sqrt(__pp * (__pp - self.__sides[0]) * (__pp - self.__sides[1]) * (__pp - self.__sides[2]))
        return _square


class Cube(Figure):
    sides_count = 12


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