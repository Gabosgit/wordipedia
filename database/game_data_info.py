'''
This dict is a dynamic dict, depending on how many players gonna join
This dict will be generated new after every game cycle
This script also stores the given word
'''
given_word = ""
players_dict = {"player_name":{ "word_freq": 25,
                                "wiki_page": "",
                                "stay": False,
                                "trials": 2
                              }
                }
starting_wikipage = ""
winners = []