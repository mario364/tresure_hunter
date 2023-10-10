from adventurelib import *

item1 = Item('apple')
room1 = Room('Тесты с предметами')
room1.items = Bag([item1])
current_room = room1
inventory = Bag()
@when('take ITEM')
def take(item):
    global current_room
    obj = current_room.items.take(item)
    print(obj)
    if not obj:
        print('Здесь нет такого')
    else:
        print(f'Вы взяли {item}')
        inventory.add(obj)

@when('inv')
def inv():
    print(*inventory)

@when('eat ITEM')
def eat(item):
    print(inventory)
    obj = inventory.take(item)
    print(inventory)
    print(obj)



start()