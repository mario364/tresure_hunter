from adventurelib import *
from person import *

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
    print(thing)
    print(f'you take {thing}')
    hero.inventory.add(thing)

@when('find')
def find():
    hero.inventory.take('hat')
start()
