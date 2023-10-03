from src.dice import DiceGame


def test_default_values():
    game = DiceGame()
    assert game.num_players == 4
    assert game.num_dice == 5
    assert game.num_sides == 6


def test_custom_values():
    game = DiceGame(num_players=2, num_dice=3, num_sides=8)
    assert game.num_players == 2
    assert game.num_dice == 3
    assert game.num_sides == 8


def test_roll_single_dice():
    game = DiceGame()
    rolled_value = game.roll_single_dice()
    assert 1 <= rolled_value <= 6  # Assuming max num_sides is 6


def test_roll_dice_for_player():
    game = DiceGame()
    rolls = game.roll_dice_for_player()
    assert len(rolls) == 5
    for roll in rolls:
        assert 1 <= roll <= 6


def test_conduct_round():
    game = DiceGame()
    game.conduct_round()
    assert len(game.df_data['Player_1']) == 1
    assert len(game.df_data['Round_Winners']) == 1


def test_find_max_rounds_winners():
    game = DiceGame()
    game.df_data = {'Round_Winners': [['Player_1', 'Player_2'], ['Player_1', 'Player_2']]}
    winners, wins = game.find_max_rounds_winners()
    assert winners == ['Player_1', 'Player_2']
    assert wins == 2


def test_str_with_single_winner():
    game = DiceGame()
    game.df_data = {'Round_Winners': [['Player_1', 'Player_2'], ['Player_1', 'Player_3']]}
    result = str(game)
    assert result == 'Player_1 wins the most rounds: 2'


def test_str_with_multiple_winners():
    game = DiceGame()
    game.df_data = {'Round_Winners': [['Player_1', 'Player_3'], ['Player_1', 'Player_3']]}
    result = str(game)
    assert result == 'Player_1, Player_3 wins the most rounds: 2 each'
