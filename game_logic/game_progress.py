import sys
sys.path.insert(0, '/project/workspace/database')
sys.path.insert(0, '/project/workspace/ui')

import ui.print_game_info as print_game_info
import ui.user_input as user_input
import database.game_data_info as game_data_info
import database.random_word as random_word
import database.article as article
import database.word_counter as word_counter
from database.article import set_random_links
from database.article import get_specified_article
from database.article import get_random_article
from ui.color_library import *

def gameplay():
    #initialize the game:
    # clear the winners list:
    game_data_info.winners.clear()
    #reset given_word to empty string
    game_data_info.given_word = ""
    #reset the starting_wikipage to empty string
    game_data_info.starting_wikipage = ""
    #reset the player_dict to empty dictionary
    if game_data_info.players_dict:
        game_data_info.players_dict.clear()

    #ask how many players (2 players minimum and 4 players maximal)
    #ask for names of the players
    players = user_input.players_dict()

    #add the players from players_dict to our player_dict in the game_data_info
    for player in players:
        if player not in game_data_info.players_dict:
            game_data_info.players_dict[player] = {"word_freq":0, "wiki_page":"", "stay":False, "trials": 2}

    #announce the new players on the display
    print_game_info.print_start_announcement(game_data_info.players_dict)

    #Generate random word from word list database for given_word and
    #store the randomized word into given_word variable in the game_data_info.py
    game_data_info.given_word = random_word.random_word()
    #game_data_info.given_word = "the"
    #Generate starting wiki page, store the starting wiki page into player dictionary
    random_article_name, random_article_content, random_article_links = get_random_article()
    game_data_info.starting_wikipage = random_article_name

    #Update the starting wiki page to players.dict in database
    for player in game_data_info.players_dict:
        game_data_info.players_dict[player]["wiki_page"] = random_article_name

    #Display the given word and the starting wikipedia pages
    print_game_info.print_given_word()
    print_game_info.print_starting_wiki_page()

    #main loop start
    stay_counter = 0
    while True:
        for player, info in game_data_info.players_dict.items():
            #Check if every player wants to stay or move on to the next
                #if the player choose to skip and still has the skipping trials left:
            if info["stay"] == False:
                print("\n" + bk_b(f" {player} ") + ", it is your turn----------->")
                if not user_input.check_input() and info["trials"] > 0:
                    #Show the player the list of linked articles to the player's current wiki page
                    article, article_content, article_links = get_specified_article(info["wiki_page"])
                    wiki_list = set_random_links(article_links)[:50]
                    for article_name in wiki_list :
                        print(article_name)
                    #let user choose a wiki title and update that into wiki_page in database
                    article_index = user_input.user_wiki_title_choose(wiki_list)
                    info["wiki_page"] = wiki_list[article_index-1].split(".")[1]
                    print(info["wiki_page"])
                    #Reduce the jumping trials for 1 jump less
                    info["trials"] = info["trials"] - 1
                    print(r_bk(" Skipping attempts left for") + b_bk(f" {player} ") + f": {info['trials']}")
                    if info["trials"] == 0:
                        stay_counter += 1
                        info["stay"] = True
                else:
                    info["stay"] = True
                    stay_counter += 1
                    print(b_bk(f" {player}'s ") + " final page is:" + g_bk(f" {info['wiki_page']} "))
                    article, article_content, article_links = get_specified_article(info['wiki_page'])
                    info["word_freq"] = word_counter.count_word(article_content, game_data_info.given_word )
            else:
                print(f"\n{player} already finalised the decision----->")
                print(f"Chosen Page: {info['wiki_page']}")
        if stay_counter == len(game_data_info.players_dict):
            break
    # Get the max occurence and announce the winner
    rank_lst = sorted(game_data_info.players_dict, key=lambda key: game_data_info.players_dict[key]["word_freq"],
                      reverse=True)
    # Check if there are multiple winners
    # if the word_freq of the top player in rank_lst equals
    # the word_freq of other players in players_dict database
    # it means that there are more than 1 winner,
    # since they share the same word_freq
    for player, info in game_data_info.players_dict.items():
        if info["word_freq"] == game_data_info.players_dict[rank_lst[0]]["word_freq"]:
            game_data_info.winners.append(player)

    print_game_info.print_winner()
