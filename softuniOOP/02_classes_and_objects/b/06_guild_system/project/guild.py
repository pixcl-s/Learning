
from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for x in self.players:
            if x.name == player_name:
                self.players.remove(x)
                x.guild = "Unaffiliated"
                return f"Player {x.name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        to_return = f"Guild: {self.name}"
        for y in self.players:
            to_return += f"\n{y.player_info()}"
        return to_return
