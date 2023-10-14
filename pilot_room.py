from items import *
from func import *
import stats_func
from adventurelib import *
from person import *

left_room = Room('Левая комната. Тест 1')
right_room = Room('Правая комната. Тест 1')
center_room = Room('Центральная комната с дверью. Тест 1')
current_room = start_room = Room('Это стартовая комната')
start_room.items = Bag()
left_room.items = Bag([Chest('chest')])
right_room.items = Bag([Apple('apple')])
center_room.items = Bag([Door('door')])

say(current_room)


@when('left')
def go_left():
    global current_room
    current_room = left_room
    print(current_room)
    unpacking_room(current_room.items)


@when('right')
def go_right():
    global current_room
    current_room = right_room
    print(current_room)
    unpacking_room(current_room.items)


@when('center')
def go_center():
    global current_room
    current_room = center_room
    print(current_room)
    unpacking_room(current_room.items)


@when('use ITEM')
def use(item):
    if item in hero.inventory:
        hero.inventory.take(item).use(hero)
    else:
        print('Нет предмета')


@when('interact ITEM')
def interact(item):
    if item in current_room.items:
        current_room.items.take(item).interact()
    else:
        print('Тут нету такого')


@when('take ITEM')
def take(item):
    global current_room
    if item in current_room.items:
        print(f'Вы взяли {item}')
        hero.inventory.add(current_room.items.take(item))

    else:
        print('Здесь нет такого')


start()
