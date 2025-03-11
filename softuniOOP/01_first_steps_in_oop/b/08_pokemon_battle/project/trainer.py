from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for x in self.pokemons:
            if pokemon_name == x.name:
                self.pokemons.remove(x)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for y in self.pokemons:
            to_return += f"\n- {y.pokemon_details()}"
        return to_return
