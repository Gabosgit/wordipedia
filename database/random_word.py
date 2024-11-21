import random
import json
from database.article import get_random_article
'''
generate a random word from the given hardcoded random_words_list.json
'''

with open('database/random_words_list.json', 'r') as words_file:
    data_words = words_file.read()
    list_words = json.loads(data_words)


def random_word():
    selected_word = random.choice(list_words)
    return selected_word