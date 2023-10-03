import random
from collections import defaultdict


class DiceGame:
    """
    A class representing a simple dice game with multiple players.

    Parameters:
    - num_players (int): Number of players in the game (default is 4).
    - num_dice (int): Number of dice each player rolls in a round (default is 5).
    - num_sides (int): Number of sides on each dice (default is 6).
    """

    def __init__(self, num_players=4, num_dice=5, num_sides=6):
        self.num_players = num_players
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.df_data = defaultdict(list)

    def roll_single_dice(self):
        """
        Simulate rolling a single dice with a random outcome.

        Returns:
                int: Randomly generated number representing the dice roll.
        """
        return random.randint(1, self.num_sides)

    def roll_dice_for_player(self):
        """
        Simulate rolling multiple dice for a single player.

        Returns:
        list: A list containing the outcomes of rolling each dice.
        """
        rolls = []
        for i in range(self.num_dice):
            single_dice = self.roll_single_dice()
            rolls.append(single_dice)
        return rolls

    def conduct_round(self):
        """
        Conduct a round of the dice game for all players, storing the outcomes.

        Returns:
        defaultdict: A dictionary containing player names as keys and their dice roll outcomes as values.
        """
        for j in range(self.num_players):
            self.df_data[f'Player_{j + 1}'].append(self.roll_dice_for_player())
        return self.df_data

    def calculate_player_sums(self):
        """
        Calculate the sum of dice roll outcomes for each player.

        Returns:
        defaultdict: A dictionary containing player names as keys and the sum of their dice roll outcomes as values.
        """
        player_sums = defaultdict(int)
        for player, dice_rolls in self.df_data.items():
            for rolls in dice_rolls:
                player_sums[player] += sum(rolls)
        return player_sums

    def determine_winner(self):
        """
        Determine the winner(s) of the dice game based on the highest sum of dice roll outcomes.

        Returns:
        list: A list containing player names who have the highest sum of dice roll outcomes.
        """
        player_sums = self.calculate_player_sums()
        max_sum = max(player_sums.values())
        max_players = [player for player, sum_value in player_sums.items() if sum_value == max_sum]
        return max_players

    def __str__(self):
        """
        Return a formatted string representing the winners of the game.

        If there are multiple winners, the function joins their names with commas
        and returns a string in the format "{winner1}, {winner2}, ... are the winners!".
        If there is only one winner, the function returns a string in the format
        "{winner} is a winner!".

        Returns:
            str: Formatted string indicating the winners of the game.
        """
        winner = self.determine_winner()
        if len(winner) > 1:
            winners = ', '.join(winner)
            return f'{winners} are the winners!'
        else:
            return f'{winner[0]} is a winner!'
