from random import randint
from adventurelib import Item
from person import *


class Chest(Item):
    @staticmethod
    def interact():
        print(f'Вы открыли сундук и получили {randint(1, 10)}')
        hero.coins += randint(1, 1)


class Apple(Item):
    @staticmethod
    def use(person: Hero):
        if person.hp == person.max_hp:
            print('У вас полные hp')
        if person.hp + 3 <= person.max_hp:
            print('Вы восстановили hp')
            person.hp += 3


class Door(Item):
    @staticmethod
    def interact():
        print('Вы открыли дверь')

