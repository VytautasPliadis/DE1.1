import streamlit as st
from dice import Dice
import inspect


def toggle_game_state():
    st.session_state.game_state = not st.session_state.game_state


# Layout configuration
st.set_page_config(
    page_title='🎲 DE 1.1',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = False
if 'game' not in st.session_state:
    st.session_state.game = Dice()

# Project title and description
st.title('🎲 DE 1.1')
st.caption('A DICE GAME by Vytautas Pliadis')
st.caption('Turing College. Module 1: Introduction to Data Engineering. Sprint:1 Intermediate Python & Git')
if not st.session_state.game_state:
    with st.expander("Learn How to Play:"):
        st.markdown("1. Edit the game settings and click 'Apply Settings' to confirm.\n"
                    "\n     Select the number of players for the game.\n"
                    "\n     Choose how many dice each player will use in a single throw.\n"
                    "\n     Enter the number of sides on each die.\n"
                    "\n2. CClick the 'Roll Dice' button to record players' scores within a table. "
                    "You can push the button multiple times.\n"
                    "\n3. Press the 'End Game' button to determine the winner.")
    with st.expander("Check The Main Code:"):
        # Get the source code of the entire module
        module_source_code = inspect.getsource(Dice)
        st.code(module_source_code)

    # Define layout columns
col1, col2 = st.columns(2)
if st.session_state.game_state:
    with col1:
        st.caption('PLAYERS TOTAL SCORE TABLE:')

    with col2:
        st.caption('ROLL ROUND RECORD:')

# Sidebar UI
with st.sidebar:
    st.sidebar.markdown('## SETTINGS:')
    # Sliders
    num_players = st.slider('Number of players', 2, 4, 4, disabled=st.session_state.game_state)
    num_dice = st.slider('Number of dice', 1, 5, 5, disabled=st.session_state.game_state)
    num_sides = st.slider('Number of sides on a single die', 4, 100, 6, disabled=st.session_state.game_state)

    # Buttons
    settings_btn = st.button('Apply Settings', use_container_width=True, disabled=st.session_state.game_state,
                             on_click=toggle_game_state)
    start_btn = st.button('Roll Dice', use_container_width=True, disabled=not st.session_state.game_state)
    stop_btn = st.button('End Game', use_container_width=True, disabled=not st.session_state.game_state,
                         on_click=toggle_game_state)

# Game logic
if settings_btn:
    st.sidebar.info('Now "Roll Dice" as many times as you want')
    # Initialize a new game
    st.session_state.game = Dice(num_players, num_dice, num_sides)

if start_btn:
    game_round = st.session_state.game.round_record()
    game_record = st.session_state.game.get_player_sums()  # Then call this method
    with col1:
        st.dataframe(game_record, use_container_width=True)

    with col2:
        st.dataframe(game_round, use_container_width=True, hide_index=False)

if stop_btn:
    try:
        winner = st.session_state.game.get_winner()
        if len(winner) > 1:
            winners = ', '.join(winner)
            st.success(f'{winners} are the winners!')
        else:
            st.success(f'{winner[0]} is a winner!')
    except:
        st.sidebar.warning('Roll the dice ant least ones. Click "Apply Settings" to start the game.')
