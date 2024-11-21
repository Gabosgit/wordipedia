def count_word(page_text, word):
    """ 
        This function take a text of a page from get_random_article()
        Count the occurences of the given word
        The word argument should be the return from random_word.py
    """
    occurences = page_text.count(word)
    return occurences

# random_article_name, random_article_content, random_article_links = get_random_article()