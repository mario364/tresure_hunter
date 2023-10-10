from adventurelib import *
from func import unpacking_inventory
from person import hero


@when('hp')
def show_hp():
    print(hero.current_hp)


@when('stats')
def show_stats():
    say(f'''Здоровье: {hero.hp}
    Взлом: {hero.breaking_skill}
    Ловкость: {hero.agility_skill}
    Интеллект: {hero.intellect_skill}
    Монет: {hero.coins}''')


@when('inv')
def show_inv():
    unpacking_inventory(hero.inventory)
