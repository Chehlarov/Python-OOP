from project.pokemon import Pokemon
from typing import List


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        else:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in list(self.pokemon):
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        trainner_info = [
            f"Pokemon trainer {self.name}",
            f"Pokemon count {len(self.pokemon)}"
        ]
        pokemon_info = [f"- {p.pokemon_details()}" for p in self.pokemon]
        return '\n'.join(trainner_info + pokemon_info)+ '\n'
