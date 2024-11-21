'''
This is where the main game loop logic is defined for 
the solo mode for now it is a proposal
'''
'''
import sys
sys.path.insert(0, '/project/workspace/database')
sys.path.insert(0, '/project/workspace/ui')
import ui.print_game_info as print_game_info
import ui.user_input as user_input
import database.game_data_info as game_data_info
'''
from ..ui.user_input import count_word
#### initialize the game: 
# given_word_list = []
# given_words_freq_list = []
# index_max_freq_word = 0
# index_chosen_word = 0

#### ask how many players (if 1 player, call game_solo_progress.py)

#### step 1
#### Generate random word from word list database and
#### append 3 randomized words into given_words_list
#### Generate starting wiki page, store into wiki_page_name

#### step 2
#### Print the 3 given words
#### Print the wikipedia page

#### step 3
#### User inputs the index for the chosen word, 
#### (the word they think will have a higher num of occurrences in that wiki page)

#### step 3.5
#### Allow the user two chances to skip to another wiki page

#### step 4
#### Calculate num of occurrences for each word in the wiki page
#### Append to given_words_freq_list, obtain max value index
#### index_max_freq_word = max(given_words_freq_list)
#### Compare with index from given_words_list

#### step 5
#### Display freq for each word:
#### print(dict(zip(given_word_list, given_words_freq_list)))
#### print("And the result is...")
#### if index_max_freq_word == index_chosen_word
####     print("You won!")
#### else:
####     print("You lost... Good luck next time!")