# [DE 1.1: Dice Game 🎲](https://vytautaspliadis-de1-1-app-6ggr12.streamlit.app/)

Project for Turing College's Module 1: Introduction to Data Engineering, Sprint 1: Intermediate Python & Git.
- [Play the Dice Game](https://vytautaspliadis-de1-1-app-6ggr12.streamlit.app/)

## Project Overview
This Python application simulates a simple dice game for multiple players. Players can customize the game settings, roll dice, and determine the winner based on the highest sum of dice roll outcomes. 
The game is implemented using the Streamlit web framework and consists of three main files:

- **app.py:** The main application file containing the Streamlit web interface and game logic.
- **dice.py:** A module defining the `DiceGame` class, which represents the game's core functionality.
- **test_dice.py** A unit tests for the `DiceGame` class functionality.

## How to Play 

### Configure Game Settings:

- Select the number of players for the game.
- Choose how many dice each player will use in a single throw.
- Enter the number of sides on each die.
- Click 'Apply Settings' to confirm your choices.

### Roll Dice:

- After applying the settings, click 'Roll Dice' to record players' scores within a table.
- You can click the button multiple times to simulate multiple rounds.

### Determine the Winner:

- Press the 'End Game' button to determine the winner(s) based on the highest total score.
- The winner(s) will be displayed in the sidebar.
- To restart the game, click 'Apply Settings' again.

## Summary of DiceGame class functionality

- **Initialization:**
The class is initialized with parameters for the number of players, dice, and sides on each die. Default values are set for 4 players, 5 dice per player, and 6 sides on each die.

- **Dice Rolling:**
The class provides methods to simulate rolling a single dice and rolling multiple dice for a player. Dice outcomes are generated randomly.

- **Game Rounds:**
The `conduct_round` method conducts a round of the game for all players, storing the dice roll outcomes for each player in a dictionary.

- **Scoring:**
The `calculate_player_sums` method calculates the sum of dice roll outcomes for each player and returns a dictionary with player names as keys and their total scores as values.

- **Determining the Winner:**
The `determine_winner` method identifies the winner(s) based on the highest total score. If there are multiple players with the same highest score, all of them are considered winners.

- **Data Storage:**
The class uses a defaultdict to store dice roll outcomes for each player, allowing easy access and manipulation of the game data.

Happy Rolling! 🎲
