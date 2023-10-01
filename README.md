# [DE 1.1: Dice Game 🎲](https://vytautaspliadis-de1-1-app-6ggr12.streamlit.app/)

Project for Turing College's Module 1: Introduction to Data Engineering, Sprint 1: Intermediate Python & Git.

## Project Overview
This Python application simulates a simple dice game for multiple players. Players can customize the game settings, roll dice, and determine the winner based on the highest sum of dice roll outcomes. 
The game is implemented using the Streamlit web framework and consists of three main files:

- **app.py:** The main application file containing the Streamlit web interface and game logic.
- **dice.py:** A module defining the `DiceGame` class, which represents the game's core functionality.
- **test_dice.py A unit tests for the `DiceGame` class functionality.

## How to Play 

### Configure Game Settings:

1. Select the number of players for the game.
2. Choose how many dice each player will use in a single throw.
3. Enter the number of sides on each die.
4. Click 'Apply Settings' to confirm your choices.

### Roll Dice:

- After applying the settings, click 'Roll Dice' to record players' scores within a table.
- You can click the button multiple times to simulate multiple rounds.

### Determine the Winner:

- Press the 'End Game' button to determine the winner(s) based on the highest total score.
- The winner(s) will be displayed in the sidebar.
- To restart the game, click 'Apply Settings' again.

## Source Code

You can explore the source code of the `DiceGame` class in `dice.py` to understand the game's internal logic.
[View DiceGame Class Source Code](link_to_dice.py)


[Play the Dice Game](https://vytautaspliadis-de1-1-app-6ggr12.streamlit.app/)
