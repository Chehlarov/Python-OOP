class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        player_name = player.username
        names = list(map(lambda x: x.username, self.players))
        if player_name in names:
            raise ValueError(f"Player {player_name} already exists!")
        self.count += 1
        self.players.append(player)

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        # player_to_remove = list(filter(lambda x: x.username == player_name, self.players))[0] #use the next row
        # player_to_remove = [p for p in self.players if p.username == player_name][0]
        player_to_remove = self.find(player_name)
        self.count -= 1
        self.players.remove(player_to_remove)

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player
