from dice import DiceGame
import unittest
from collections import defaultdict


class TestDiceGame(unittest.TestCase):
    def setUp(self):
        self.game = DiceGame(num_players=4, num_dice=5, num_sides=6)

    def test_roll_single_dice(self):
        result = self.game.roll_single_dice()
        self.assertTrue(1 <= result <= 6)

    def test_roll_dice_for_player(self):
        rolls = self.game.roll_dice_for_player()
        self.assertEqual(len(rolls), 5)
        for roll in rolls:
            self.assertTrue(1 <= roll <= 6)

    def test_conduct_round(self):
        data = self.game.conduct_round()
        self.assertIsInstance(data, defaultdict)
        self.assertEqual(len(data.keys()), 4)
        for player, rolls in data.items():
            self.assertEqual(len(rolls), 1)
            for roll in rolls[0]:
                self.assertTrue(1 <= roll <= 6)

    def test_calculate_player_sums(self):
        self.game.df_data = {
            'Player_1': [[1, 2, 3, 4, 5]],
            'Player_2': [[6, 6, 6, 6, 6]],
            'Player_3': [[3, 3, 3, 3, 3]],
            'Player_4': [[2, 2, 2, 2, 2]],
        }
        player_sums = self.game.calculate_player_sums()
        self.assertEqual(player_sums['Player_1'], 15)
        self.assertEqual(player_sums['Player_2'], 30)
        self.assertEqual(player_sums['Player_3'], 15)
        self.assertEqual(player_sums['Player_4'], 10)

    def test_determine_winner(self):
        self.game.df_data = {
            'Player_1': [[4, 4, 4, 4, 4]],
            'Player_2': [[2, 2, 2, 2, 2]],
            'Player_3': [[3, 3, 3, 3, 3]],
            'Player_4': [[4, 4, 4, 4, 4]],
        }
        winners = self.game.determine_winner()
        self.assertEqual(winners, ['Player_1', 'Player_4'])


if __name__ == '__main__':
    unittest.main()
