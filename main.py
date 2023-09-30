import streamlit as st
from collections import defaultdict
import random


# Function to toggle game state
def change_game_state():
    game_state = st.session_state.game_state
    st.session_state.game_state = not game_state


def show_table(df_data):
    if not df_data:
        # Help widget
        with st.expander("Learn How to Play:"):
            st.markdown("1. Edit the game settings and click 'Apply Settings' to confirm.\n"
                        "\n     Select the number of players for the game.\n"
                        "\n     Choose how many dice each player will use in a single throw.\n"
                        "\n     Enter the number of sides on each die.\n"
                        "\n2. Click the 'Throw Dice' button to record players' scores in a table. You can push the button multiple times.\n"
                        "\n3. Press the 'End Game' button to determine the winner.")
    else:
        st.table(df_data)


def random_dice_value(dice_side_num, dice_num):
    score = []
    for i in range(dice_num):
        single_dice_value = random.randint(2, dice_side_num)
        st.sidebar.write(f'Dice {i+1} value: {single_dice_value}')
        score.append(single_dice_value)
    return sum(score)


def score_records(df_data):
    for i in range(players_num):
        st.sidebar.markdown('---')
        st.sidebar.write(f'Player_{i + 1}:')
        df_data[f'Player_{i + 1}'].append(random_dice_value(dice_side_num,dice_num))


def return_winner(df_data):
    # Calculate total values for each player
    total_values = {}
    for player, values in df_data.items():
        total_values[player] = sum(values)
    max_value = max(total_values.values())
    # Find all players with the maximum total value
    winners = [player for player, value in total_values.items() if value == max_value]
    if len(winners) > 1:
        winners = ', '.join(winners)
        st.sidebar.success(f'{winners} are the winners!')
    else:
        st.sidebar.success(f'{winners[0]} is a winner!')


# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = False
if 'df_data' not in st.session_state:
    st.session_state.df_data = defaultdict(list)

# Title of project
st.title('🎲 DE 1.1')
st.caption('A DICE GAME by Vytautas Pliadis')
st.caption('Turing College. Module 1: Introduction to Data Engineering. Sprint:1 Intermediate Python & Git')

# SETTINGS UI
st.sidebar.markdown('## SETTINGS:')
players_num = st.sidebar.slider('Enter a number of players:', min_value=2, max_value=5, value=5,
                                disabled=st.session_state.game_state)
dice_num = st.sidebar.slider('Enter a number of dices:', min_value=1, max_value=5, value=1,
                             disabled=st.session_state.game_state)
dice_side_num = st.sidebar.slider('Enter a sides number of a single dice:', min_value=3, max_value=100, value=6,
                                  disabled=st.session_state.game_state)

# Button UI
settings_btn = st.sidebar.button('Apply Settings', use_container_width=True, key='settings',
                                 disabled=st.session_state.game_state, on_click=change_game_state)
start_btn = st.sidebar.button('Throw Dice', use_container_width=True, key='start',
                              disabled=not st.session_state.game_state)
stop_btn = st.sidebar.button('End Game', use_container_width=True, key='stop',
                             disabled=not st.session_state.game_state, on_click=change_game_state)

# Dictionary
if start_btn:
    score_records(st.session_state.df_data)
if stop_btn:
    winner = return_winner(st.session_state.df_data)
    st.session_state.df_data = defaultdict(list)

# Table to display results
show_table(st.session_state.df_data)