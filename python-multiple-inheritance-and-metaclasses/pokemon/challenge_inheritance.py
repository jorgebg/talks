"""
Change the damage of the moves depending on the types and levels.
Remember Fire beats Water.
"""


class Type:
    pass


class Fire(Type):
    pass


class Water(Type):
    pass


class Move:

    power = 5

    def __init__(self, pokemon):
        self.pokemon = pokemon

    def attack(self, pokemon):
        pokemon.hp -= self.power


class Ember(Fire, Move):
    pass


class Pokemon:

    def __init__(self, level=1):
        self.level = level
        self.hp = 30
        self.move = None

    def attack(self, pokemon):
        self.move.attack(pokemon)


class Charmander(Fire, Pokemon):

    def __init__(self, level=1):
        super().__init__(level)
        self.move = Ember(self)


class Squirtle(Water, Pokemon):
    pass


char = Charmander()
squir = Squirtle()

char.attack(squir)
squir.hp
