from ui.color_library import *

def input_min_and_max_int(prompt, min_num, max_num):
    """ The function checks if the user entered a min and max number.
        It also checks if the input is a positive integer.
        If the input does not meet these conditions, it raises an Exception."""
    while True:
        try:
            input_user = int(input(prompt))
            if min_num > input_user or input_user > max_num:
                raise Exception(f"The minimum number of players is {min_num}\n"
                                f"The maximum number of players is {max_num}\n"
                                "A positive number is expected\n")
        except ValueError:
            print(f"Expected a positive integer")
        except Exception as error:
            print(error)
        else:
            return input_user


def if_input_empty(prompt):
    """ This function checks that the input (player name) is not empty.
        If the input is empty it prints a warning message """
    while True:
        user_input = input(prompt)
        if user_input == '':
            print('Field is empty')
        else:
            return user_input


def players_dict():
    """ This function gets the number of users from input_min_and_max_int()
        It creates a dictionary for each player with the data:
        name = player name, word_frequency = word frequency :) and stay_title = player's final choice of title.
        It checks that there are no repeated player names. It prints a warning if the name is not available.
        RETURNS {'player_1_name': {"freq_word":0, "wiki_page":""}} 
    """
    dict_players = {}
    list_player_name = [] # to check that the names of players are not repeated
    number_of_players = input_min_and_max_int(f"{bk_y(' Please, enter the number of players (min. 2 | max. 4): ')}\n", 2, 4)
    for player_num in range(1, number_of_players+1): # It creates a dictionary for each player
        while True:
            player_name = if_input_empty(f"Please, enter the name of {bk_c(f' player {player_num}: ')}")
            if player_name in list_player_name:
                print("This name is not available")
            else:
                dict_players[player_name] = {'freq_word': 0, 'wiki_page': ''}
                list_player_name.append(player_name)
                break
    return dict_players
#players_dict()

#wiki_list_example_for_testing = [1,2,3,4,5]
def user_wiki_title_choose(wiki_list):
    """ This function takes a list 'wiki links' as argument.
        It prompts the player for an option from the list
        Returns the index of the list chosen by the user. """
    wiki_list_length = len(wiki_list)
    user_choose = input_min_and_max_int(f"{bk_y(f' Please, choose a wiki title and enter its list number (1 - {wiki_list_length}): ')}\n", 1, wiki_list_length)
    return user_choose
#print(user_wiki_title_choose(wiki_list_example_for_testing))


def check_input():
    """
    User should enter 1 to "stay" or 2 to "skip"
    Return True if stay
    Return False if skip
    """
    user_input = input_min_and_max_int(f"Enter {m_bk(' 1 to stay ')} or {c_bk(' 2 to skip ')}", 1, 2)
    if user_input == 1:
        return True
    elif user_input == 2:
        return False
#print(check_input())
