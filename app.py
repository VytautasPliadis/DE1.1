import streamlit as st
from src.dice import DiceGame  # Importing DiceGame class from src module
import inspect


# Function to toggle game state
def toggle_game_state():
    st.session_state.game_state = not st.session_state.game_state


# Streamlit page configuration
st.set_page_config(
    page_title='🎲 DE 1.1',
    initial_sidebar_state="expanded",
)

# Initialize session state variables if they do not exist
if 'game_state' not in st.session_state:
    st.session_state.game_state = False
if 'game' not in st.session_state:
    st.session_state.game = DiceGame()  # Creating an instance of DiceGame class

# Project title and description
st.title('🎲 DE 1.1')
st.caption('A DICE GAME by Vytautas Pliadis')
st.caption('Turing College. Module 1: Introduction to Data Engineering. Sprint:1 Intermediate Python & Git')

# Display game instructions and source code in an expander if the game is not active
if not st.session_state.game_state:
    with st.expander("Learn How to Play:"):
        st.markdown("1. Edit the game settings and click 'Apply Settings' to confirm:\n"
                    "\n     - Select the number of players for the game.\n"
                    "\n     - Choose how many src each player will use in a single throw.\n"
                    "\n     - Enter the number of sides on each die.\n"
                    "\n2. Click the 'Roll Dice' button to record players' scores within a table. "
                    "You can push the button multiple times.\n"
                    "\n3. Press the 'End Game' button to determine the winner.")
    with st.expander("Check The Main Code:"):
        # Get and display the source code of the DiceGame class
        module_source_code = inspect.getsource(DiceGame)
        st.code(module_source_code)

# Sidebar UI for game settings
with st.sidebar:
    st.sidebar.markdown('## SETTINGS:')
    # Sliders for number of players, src, and sides
    num_players = st.slider('Number of players', 2, 5, 3, disabled=st.session_state.game_state)
    num_dice = st.slider('Number of src', 1, 5, 1, disabled=st.session_state.game_state)
    num_sides = st.slider('Number of sides on a single die', 4, 100, 6, disabled=st.session_state.game_state)

    # Buttons for applying settings, rolling src, and ending the game
    settings_btn = st.button('Apply Settings', use_container_width=True, disabled=st.session_state.game_state,
                             on_click=toggle_game_state)
    start_btn = st.button('Roll Dice', use_container_width=True, disabled=not st.session_state.game_state)
    stop_btn = st.button('End Game', use_container_width=True, disabled=not st.session_state.game_state,
                         on_click=toggle_game_state)

# Game logic based on button clicks
if settings_btn:
    st.sidebar.info('Now "Roll Dice" as many times as you want')
    # Initialize a new game with user-defined settings
    st.session_state.game = DiceGame(num_players, num_dice, num_sides)

if start_btn:
    # Conduct a game round and display player scores and src rolls
    game_round = st.session_state.game.conduct_round()
    st.caption('ROLL ROUND DICE TABLE')
    st.dataframe(game_round, use_container_width=True, hide_index=False)

if stop_btn:
    try:
        st.sidebar.success(st.session_state.game)
    except Exception as e:
        st.sidebar.warning(f'Roll the src at least once.\n'
                           f'\nClick "Apply Settings" to restart the game.\n'
                           f'\nAn unexpected error occurred: {e}\n')
        pass
