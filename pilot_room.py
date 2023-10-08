from adventurelib import *
from person import *
from items import *

room1 = Room('Левая комната с дверью и сундуком. Тест 1')
room2 = Room('Правая комната с яблоком и его использованием. Тест 1')
current_room = start_room = Room('Это стартовая комната')
room1.chest = True
room1.has_item = True
room2.apple = True



say(current_room)
@when('left')
def left():
    global current_room
    current_room = room1
    print(current_room)

@when('hp')
def show_hp():
    print(hero.current_hp)


@when('stats')
def show_stats():
    say(f'''Здоровье: {hero.hp}
    Взлом: {hero.breaking_skill}
    Ловкость: {hero.agility_skill}
    Интеллект: {hero.intellect_skill}''')


@when('inv')
def show_inv():
    for item in hero.inventory:
        print(item)


@when('take THING')
def take(thing):
    global current_room
    if hasattr(current_room, 'has_item'):
        print(f'you take {thing}')
        hero.inventory.append(thing)
        current_room.has_item = False


@when('use ITEM on THING')
def use(item, thing):
    print(f'you use {item} on {thing}')

@when('examine THING')
def examine(thing):
    print(f'Вы видите {thing}')

start()
