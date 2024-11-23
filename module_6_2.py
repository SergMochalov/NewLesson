class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str,  __model:str, __color:str, __engine_power:int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power


    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color=new_color

        else:
            print(f"Нельзя сменить цвет на {new_color} ")

        return self.__color
    def print_info(self):
        print(f"Модель: {self.__model} Мощность двигателя: {self.__engine_power} Цвет: {self.__color} Владелец:{self.owner} ")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()