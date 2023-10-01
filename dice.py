from collections import defaultdict
import random

class Dice:
    def __init__(self, num_players=5, num_dice=5, num_sides=6):
        self.num_players = num_players
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.df_data = defaultdict(list)

    def single_dice_value(self):
        return random.randint(2, self.num_sides)

    def player_roll(self):
        rolls = []
        for i in range(self.num_dice):
            single_dice = self.single_dice_value()
            rolls.append(single_dice)
        return rolls

    def round_record(self):
        for j in range(self.num_players):
            self.df_data[f'Player_{j + 1}'].append(self.player_roll())
        print(self.df_data)
        return self.df_data

    def get_player_sums(self):
        player_sums = defaultdict(int)
        for player, dice_rolls in self.df_data.items():
            for rolls in dice_rolls:
                player_sums[player] += sum(rolls)
        return player_sums

    def get_winner(self):
        player_sums = self.get_player_sums()
        if not player_sums:
            return None  # Return None if dictionary is empty
        max_sum = max(player_sums.values())
        max_players = [player for player, sum_value in player_sums.items() if sum_value == max_sum]
        return max_players