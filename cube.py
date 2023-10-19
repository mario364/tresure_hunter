from person import hero
from random import randint


class Cube:


    @staticmethod
    def cast_cube(chart: str):
        modification = (hero.characteristic[chart] - 10) // 2
        res = randint(1, 24) + modification
        print(f'Модификатор: {modification}')
        print(f'Сумма: {res}')
        if res in range(1, 24):
            return res
        if res > 23:
            return 23



cube = Cube()
print(cube.cast_cube('breaking_skill'))


