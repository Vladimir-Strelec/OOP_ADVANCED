from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        #objects
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        current_obj = self.__add_obj_for_args_in_list(self.players, args)
        if current_obj:
            self.players += current_obj
            return f"Successfully added: {', '.join([i.name for i in current_obj])}"

    def add_supply(self, *args: Supply):
        for a in args:
            self.supplies.append(a)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__get_player_obj(self.players, player_name)
        product = self.__get_valid_product(self.supplies, sustenance_type)
        if player.need_sustenance is False:
            return f"{player_name} have enough stamina."

        if player.stamina + product.energy > 100:
            player.stamina = 100
        else:
            player.stamina += product.energy
        return f"{player_name} sustained successfully with {product.name}."



    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    @staticmethod
    def __add_obj_for_args_in_list(players, args):
        result = []
        for a in args:
            for p in players:
                if a.name == p.name:
                    break
            result.append(a)
        return result

    @staticmethod
    def __get_player_obj(players, player_name):
        for p in players:
            if p.name == player_name:
                return p


    @staticmethod
    def __get_valid_product(supplies, sustenance_type):
        if sustenance_type == "Food":
            if len(supplies) == 0:
                raise Exception("There are no food supplies left!")
            return supplies.pop()
        if sustenance_type == "Drink":
            if len(supplies) == 0:
                raise Exception("There are no drink supplies left!")
            return supplies.pop()