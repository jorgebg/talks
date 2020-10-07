class Pokemon:

    number = None

    def __init__(self, level=1):
        self.level = level
        self.hp = 30

    def moves(self):
        return []


class Pikachu(Pokemon):

    number = 25

    def moves(self):
        return ['ThunderShock', 'Growl']


Pikachu.number

pika = Pikachu()
pika.number
pika.level
pika.hp


Pokemon.number
pokemon = Pokemon()
pokemon.level
pokemon.hp
pokemon.moves()

type(Pikachu)
type(pika)

isinstance(pika, Pikachu)
isinstance(pika, Pokemon)
isinstance(pika, object)


###

class Raichu(Pikachu):

    number = 26

    def moves(self):
        return ['Agility', 'Quickattack'] + super().moves()


raichu = Raichu()
raichu.number
raichu.moves()

###


class Category:
    pass


class Grass(Category):
    pass


class Poison(Category):
    pass


class Bulbasaur(Grass, Poison, Pokemon):

    number = 1

    def moves(self):
        return ['Tackle', 'Growl']


bulba = Bulbasaur()

isinstance(bulba, Pokemon)
isinstance(bulba, Grass)
isinstance(bulba, Poison)


###

class Grass(Category):
    def moves(self):
        return ['LeechSeed']


class Poison(Category):
    def moves(self):
        return ['VineWhip']


class Bulbasaur(Grass, Poison, Pokemon):

    number = 1

    def moves(self):
        return ['Tackle', 'Growl'] + super().moves()


bulba = Bulbasaur()
bulba.moves()

###


class Grass(Category):
    def moves(self):
        return ['LeechSeed'] + super().moves()


class Poison(Category):
    def moves(self):
        return ['VineWhip'] + super().moves()


class Bulbasaur(Grass, Poison, Pokemon):

    number = 1

    def moves(self):
        return ['Tackle', 'Growl'] + super().moves()


bulba = Bulbasaur()
bulba.moves()

Bulbasaur.mro()


###


class Fire(Category):
    def moves(self):
        return ['Ember'] + super().moves()


class Charmander(Pokemon, Fire):
    number = 4


Charmander.mro()

char = Charmander()
char.moves()


class Pokemon:

    # ...

    def moves(self):
        return []


###


class Fire(Category):
    def moves(self):
        return ['Ember'] + super().moves()


class Charmander(Fire, Pokemon):
    number = 4

    def moves(self):
        return super().moves()


char = Charmander()
char.moves()


###


class Fire(Category):
    def moves(self):
        return ['Ember'] + super().moves()


class Flying(Category):
    def moves(self):
        return ['Fly'] + super().moves()


class Charmander(Fire, Pokemon):
    number = 4


class Charmeleon(Charmander):
    number = Charmander.number + 1

    def moves(self):
        return ['Flamethrower'] + super().moves()


class Charizard(Charmeleon, Flying):
    number = Charmeleon.number + 1


Charizard.mro()

chari = Charizard()
chari.moves()


###

from abc import ABCMeta, abstractmethod


class Pokemon(metaclass=ABCMeta):

    number = None

    @abstractmethod
    def moves(self):
        return []


class Pikachu(Pokemon):

    number = 25


pika = Pikachu()

###


class Pikachu(Pokemon):

    def moves(self):
        return ['ThunderShock', 'Growl']


pika = Pikachu()


###

class Pokemon:
    pass

Pokemon

Pokemon = type('Pokemon', (), {})
Pokemon

###


class MyType(type):
    def __new__(cls, name, bases, attrs):
        print(name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)


class Pokemon(metaclass=MyType):
    number = None


class Slowpoke(Pokemon):
    number = 79


Pokemon
Slowpoke


###

class PokemonMeta(type):
    N_POKEMONS = 0

    def __new__(cls, name, bases, attrs):
        if bases:
            cls.N_POKEMONS += 1
            attrs['number'] = cls.N_POKEMONS
        return super().__new__(cls, name, bases, attrs)


class Pokemon(metaclass=PokemonMeta):
    pass


class Bulbasaur(Pokemon):
    pass


class Ivysaur(Bulbasaur):
    pass


class Venusaur(Ivysaur):
    pass


Bulbasaur.number
Ivysaur.number
Venusaur.number

Pokemon.number

###
