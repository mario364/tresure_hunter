from items import *
from func import *
import stats_func
from adventurelib import *
from person import *

north_room = Room('Северная комната. Тест 1')
south_room = Room('Южная комната. Тест 1')
west_room = Room('Западная комната с дверью. Тест 1')
east_room = Room('Восточная комната. Тест кубика')
current_room = start_room = Room('Это стартовая комната')
start_room.items = Bag()
north_room.items = Bag([Chest('chest')])
south_room.items = Bag([Apple('apple')])
west_room.items = Bag([Door('door')])
east_room.items = Bag([])

say(current_room)


@when('go north')
def go_north():
    current_room = north_room
    print(current_room)
    unpacking_room(current_room.items)


@when('go south')
def go_south():
    global current_room
    current_room = south_room
    print(current_room)
    unpacking_room(current_room.items)


@when('go west')
def go_west():
    global current_room
    current_room = west_room
    print(current_room)
    unpacking_room(current_room.items)

@when('go east')
def go_east():
    global current_room
    current_room = east_room
    say(current_room)
    unpacking_room()

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
