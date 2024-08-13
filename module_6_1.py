# Домашнее задание по теме "Зачем нужно наследование"

# Задача "Съедобное, несъедобное":
# Пункты задачи:
# 1 Создайте классы Animal и Plant с соответствующими атрибутами и методами
# 2 Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
#   При необходимости переопределите значения атрибутов.
# 3 Создайте объекты этих классов.

class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False  # (съедобность)
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Flower(Plant):
    pass
 #   edible = True

class Fruit(Plant):
    edible = True



animal1 = Predator('Tiger')
animal2 = Mammal('Bull')
plant1 = Plant('Rose')
plant2 = Fruit('Apple')

print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} живой')
print(animal2.fed, f'- {animal2.name} голоден')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} помер')
print(animal2.fed, f'- {animal2.name} сыт')
