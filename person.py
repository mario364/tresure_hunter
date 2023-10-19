from adventurelib import Bag


class Hero:
    name = 'Лукас'
    level = 1
    hp = 10
    max_hp = 10
    coins = 0
    inventory = Bag()
    current_hp = hp
    characteristic = {
        "breaking_skill": 20,
        "agility_skill": 10,
        "intellect_skill": 10
    }


hero = Hero()
