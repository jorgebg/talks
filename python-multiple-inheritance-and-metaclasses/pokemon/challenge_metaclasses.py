"""
How to create a Pokedex that contains all the defined pokemon classes with metaclasses?
"""


class PokemonMeta(type):
    pass


class Pokemon(metaclass=PokemonMeta):
    pass


class Bulbasaur(Pokemon):
    pass


class Ivysaur(Bulbasaur):
    pass


class Venusaur(Ivysaur):
    pass


assert PokemonMeta.POKEMONS = [Bulbasaur, Ivysaur, Venusaur]
