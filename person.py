
class Hero:
    name = 'Лукас'
    level = 1
    hp = 10
    coins = 0
    inventory = []
    current_hp = hp
    breaking_skill = 1
    agility_skill = 1
    intellect_skill = 1

class Apple:
    hp = 3

    def eat(self):
        return self.hp

hero = Hero()


