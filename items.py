from random import choice


chest_lst = ['монетка', "драгоценность", "ключ"]
class Apple:
    hp = 3

    def use(self):
        return self.hp
    def __repr__(self):
        return 'яблоко'

class Key:
    def use(self):
        return 'Вы открыли дверь ключом'

    def __repr__(self):
        return 'Ключ'


class Chest:
    def __repr__(self):
        return 'Сундук'

    def use(self):
        return choice(chest_lst)


apple = Apple()
key = Key()
chest = Chest()
