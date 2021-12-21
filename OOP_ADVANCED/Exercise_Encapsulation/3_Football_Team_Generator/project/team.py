from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if any([x for x in self.__players if x.name == player.name]):
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for current_obj in self.__players:
            if current_obj.name == player_name:
                self.__players.remove(current_obj)
                return current_obj
        return f"Player {player_name} not found"