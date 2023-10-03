import random
from collections import defaultdict


class DiceGame:
    """
    Represents a simple dice game where players roll dice and compete to win rounds.

    Parameters:
    - num_players (int): Number of players in the game. Default is 4.
    - num_dice (int): Number of dice each player rolls in a round. Default is 5.
    - num_sides (int): Number of sides on each die. Default is 6.
    """

    def __init__(self, num_players=4, num_dice=5, num_sides=6):
        """
        Initializes the DiceGame object with the specified number of players, dice, and sides.

        Args:
        - num_players (int): Number of players in the game. Default is 4.
        - num_dice (int): Number of dice each player rolls in a round. Default is 5.
        - num_sides (int): Number of sides on each die. Default is 6.
        """
        self.num_players = num_players
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.df_data = defaultdict(list)

    def roll_single_dice(self):
        """
        Simulates the roll of a single dice.

        Returns:
        int: A random integer representing the outcome of the dice roll.
        """
        return random.randint(1, self.num_sides)

    def roll_dice_for_player(self):
        """
        Rolls the dice for a single player.

        Returns:
        list: A list of integers representing the outcomes of the dice rolls for the player.
        """
        rolls = []
        for _ in range(self.num_dice):
            single_dice = self.roll_single_dice()
            rolls.append(single_dice)
        return rolls

    def conduct_round(self):
        """
        Conducts a round of the game where players roll dice and determines the round winners.

        Returns:
        defaultdict: A dictionary containing the round winners and their corresponding dice rolls.
        """
        round_winners = []
        max_sum = 0
        for j in range(1, self.num_players + 1):
            rolls = self.roll_dice_for_player()
            self.df_data[f'Player_{j}'].append(rolls)
            player_sum = sum(rolls)
            if player_sum > max_sum:
                max_sum = player_sum
                round_winners = [f'Player_{j}']
            elif player_sum == max_sum:
                round_winners.append(f'Player_{j}')
        self.df_data['Round_Winners'].append(round_winners)
        return self.df_data

    def find_max_rounds_winners(self):
        """
        Finds the player(s) who won the most rounds in the game.

        Returns:
        tuple: A tuple containing a list of player names with the most round wins and the number of wins.
        """
        player_wins = {}
        for round_winner_list in self.df_data['Round_Winners']:
            for winner in round_winner_list:
                if winner in player_wins:
                    player_wins[winner] += 1
                else:
                    player_wins[winner] = 1

        max_wins = max(player_wins.values(), default=0)
        max_winners = [player for player, wins in player_wins.items() if wins == max_wins]

        return max_winners, max_wins

    def __str__(self):
        """
        Returns a string representation of the game result indicating the player(s) who won the most rounds.

        Returns:
        str: A formatted string indicating the winner(s) of the game and the number of rounds won.
        """

        max_winners, max_wins = self.find_max_rounds_winners()
        if len(max_winners) > 1:
            max_winners = ', '.join(max_winners)
            return f'{max_winners} wins the most rounds: {max_wins} each'
        else:
            return f'{max_winners[0]} wins the most rounds: {max_wins}'
