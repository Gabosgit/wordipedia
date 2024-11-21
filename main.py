'''
The main Wordipedia game
'''
import ui.print_game_info as print_game_info
from game_logic import game_progress

    #display a welcome message
print_game_info.print_welcome()
    #display instructions
print_game_info.print_instructions()
    #display rules
print_game_info.print_rules()
    #main game starts
game_progress.gameplay()