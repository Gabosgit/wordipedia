"""Veronica codes here :)"""
from ui.color_library import *
from database import game_data_info
# storing the info as constants for easier maintenance and debbuging:

with open("database/welcome.txt", "r", encoding = "utf-8") as welcomePath:
    welcome_message = welcomePath.read()

with open("database/instructions.txt", "r", encoding = "utf-8") as instructionsPath:
    instructions = instructionsPath.read()

with open("database/rules.txt", "r", encoding = "utf-8") as rulesPath:
    rules = rulesPath.read()


def print_welcome():
    """
    Prints welcome message from database/welcome.txt
    """
    print(welcome_message)


def print_instructions():
    """
    Prints instructions for the game from database/instructions.txt
    """
    print(instructions)

def print_rules():
    """
    Prints the rules of the game from database/rules.txt
    """
    print(rules)


def print_start_announcement(players_dict):
    """
    Prints a greeting with the player's name and designation
    """
    for player in players_dict:
        print(b_bk("Welcome ") + bk_b(f" {player} ") + b_bk(" to wordipedia game!"))

    print("\n" + y_bk("---Let's start the game! Good luck everyone!!---"))

def print_winner():
    if len(game_data_info.winners) == 1:
        print("\n" + y_bk(" And the winner is: ") + bk_y(f" {game_data_info.winners} "))
    elif 1 < len(game_data_info.winners) < len(game_data_info.players_dict):
        print(y_bk("And the winners are:"))
        for winner in game_data_info.winners:
            print(bk_y(f" {winner} "))
    elif len(game_data_info.winners) == len(game_data_info.players_dict):
            print("\n" + y_bk(" It is a tie! "))
    for player, info in game_data_info.players_dict.items():
        print(f"{player} has {info['word_freq']} word occurences")

def print_given_word(): #print the given_word from database
    print(f"The given word is:" + m_bk(f" {game_data_info.given_word} "))

def print_starting_wiki_page(): #print the starting_wiki_page from database
    print(f"The starting Wiki Page is:" + c_bk(f" {game_data_info.starting_wikipage} "))
