import random
from collections import defaultdict

import streamlit as st


def game_dictionary_reset(num_players):
    st.session_state.df_data = defaultdict(list)
    for i in range(num_players):
        st.session_state.df_data[f'Player_{i + 1}'].append(0)
    return st.session_state.df_data


def random_one_dice_value(dice_slide):
    return random.randint(1, int(dice_slide))


if 'df_data' not in st.session_state:
    game_dictionary_reset(2)

if 'game_state' not in st.session_state:
    st.session_state.game_state = False


st.title('🎲 DE 1.1')
st.caption('A DICE GAME')
st.caption('Turing College, Module 1: Introduction to Data Engineering. Sprint:1 Intermediate Python & Git')

st.sidebar.markdown('## SETTINGS:')

# Slider for number of payers
players_num = st.sidebar.slider('SELECT NUMBER OF PLAYERS:', min_value=1, max_value=5, value=2, disabled=st.session_state.game_state)

# Slider for number of dices
dice_num = st.sidebar.slider('SELECT NUMBER OF DICES:', min_value=1, max_value=5, value=2,disabled=st.session_state.game_state)

# Slider for type of dices
dice_slide = st.sidebar.slider('SELECT HOW MANY SIDES A DICE CAN HAVE:', min_value=2, max_value=100, value=6, disabled=st.session_state.game_state)

# Button. Throw the dices
throw_dice_btn = st.button('Click me to trow the dices!', key='button1', use_container_width=True,disabled=not st.session_state.game_state)

# Button. Apply and reset the game
restart_btn = st.sidebar.button('Apply settings and start new game', key='button2', use_container_width=True,disabled=st.session_state.game_state)
if restart_btn:
    st.session_state.game_state = True
    # Reset session_state and create dict
    game_dictionary_reset(players_num)

# Button. Stop the game
restart_btn = st.sidebar.button('End the game', key='button3', use_container_width=True,disabled=not st.session_state.game_state)
if restart_btn:
    st.session_state.game_state = False
    # Reset session_state and create dict
    game_dictionary_reset(players_num)

# Play a game
if throw_dice_btn:
    st.session_state.game_state = True
    # st.session_state.df_data= {key: random_one_dice_value(dice_slide) for key, value in st.session_state.df_data.items()}
    for i in range(players_num):
        st.session_state.df_data[f'Player_{i+1}'].append(random_one_dice_value(dice_slide))
    # st.session_state.df_data['Player_3'].append(random_dice_value)

# Table to display results
st.table(st.session_state.df_data)

# FEATURE: Write winning layer
# st.markdown('##### PLAYER_1 is winning a game')

