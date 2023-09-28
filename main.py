import streamlit as st
import random
from collections import defaultdict


def do_on_click():
    pass


st.title('DE 1.1')
st.markdown('A DICE GAME')

if 'df_data' not in st.session_state:
    st.session_state.df_data = defaultdict(list)

# Slider for number of dices
dice_num = st.sidebar.slider('SELECT NUMBER OF DICES:', min_value=1, max_value=5)

# Slider for type of dices
dice_slide = st.sidebar.slider('SELECT HOW MANY SIDES A DICE CAN HAVE:', min_value=1, max_value=100)

# Button. Throw the dices
throw_dice_btn = st.sidebar.button('Click me to trow the dices!', key='button1', use_container_width=True)

# Write result
random_numbers = []
if throw_dice_btn:
    # st.sidebar.write('Dices were trowed!')
    random_dice_value = random.randint(1, int(dice_slide))
    st.session_state.df_data['Number of dices'].append(dice_num)
    st.session_state.df_data['Number of sides'].append(dice_slide)
    st.session_state.df_data['Score'].append(random_dice_value)

# Button. Restart the game
restart_btn = st.sidebar.button('Clear the score table', key='button2', use_container_width=True)
if restart_btn:
    st.session_state.df_data = defaultdict(list)

# Table to display results
st.table(st.session_state.df_data)

# Table to display results
st.sidebar.table(st.session_state.df_data)