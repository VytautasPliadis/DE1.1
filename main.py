import streamlit as st
import random
from collections import defaultdict


if 'df_data' not in st.session_state:
    st.session_state.df_data = defaultdict(list)

st.title('DE 1.1')
st.markdown('A DICE GAME')

# Slider for number of payers
players_num = st.sidebar.slider('SELECT NUMBER OF PLAYERS:', min_value=1, max_value=5)

# Slider for number of dices
dice_num = st.sidebar.slider('SELECT NUMBER OF DICES:', min_value=1, max_value=5)

# Slider for type of dices
dice_slide = st.sidebar.slider('SELECT HOW MANY SIDES A DICE CAN HAVE:', min_value=1, max_value=100)

# Button. Throw the dices
throw_dice_btn = st.button('Click me to trow the dices!', key='button1', use_container_width=True)

# Button. Restart the game
restart_btn = st.sidebar.button('Apply settings and start new game', key='button2', use_container_width=True)
if restart_btn:
    st.session_state.df_data = defaultdict(list)
    st.session_state.df_data['Player_1'].append(0)
    st.session_state.df_data['Player_2'].append(0)
    st.session_state.df_data['Player_3'].append(0)

# Write result
random_numbers = []
if throw_dice_btn:
    # st.sidebar.write('Dices were trowed!')
    random_dice_value = random.randint(1, int(dice_slide))
    st.session_state.df_data['Player_1'].append(dice_slide)
    st.session_state.df_data['Player_2'].append(dice_slide)
    st.session_state.df_data['Player_3'].append(dice_slide)
    st.session_state.df_data['Winner'].append('Player_1')
    # st.session_state.df_data['Number of dices'].append(dice_num)
    # st.session_state.df_data['Number of sides'].append(dice_slide)
    # st.session_state.df_data['Score'].append(random_dice_value)

# Table to display results
st.table(st.session_state.df_data)

# Table to display results
st.sidebar.table(st.session_state.df_data)
