# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

# Задача "Изменять нельзя получать":
# Пункты задачи:
# 1 Создайте классы Vehicle и Sedan.
# 2 Напишите соответствующие свойства в обоих классах.
# 3 Не забудьте сделать Sedan наследником класса Vehicle.
# 4 Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Gray']   # Допустимые цвета для окрашивания
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)         # владелец транспорта. (владелец может меняться)
        self.__model = str (__model)    # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(__engine_power)   # мощность двигателя. (мы не можем менять самостоятельно)
        self.__color = str(__color)     # название цвета. (мы не можем менять цвет автомобиля своими руками)
#
# Каждый объект Vehicle должен содержать следующий методы:
    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        # new_color = input('Новый цвет: ')
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS] # для проверки без учета регистра
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 4      # (в седан может поместиться только 4 пассажира и 1 водитель)

avto1 = Sedan('Egor', 'KIA RIO', 115, 'Green')

# Изначальные свойства
avto1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
#avto1.set_color('Мокрый асфальт')
avto1.set_color('Мокрый асфальт')
avto1.set_color('BLACK')
avto1.owner = 'Maria'

# Проверяем что поменялось
avto1.print_info()