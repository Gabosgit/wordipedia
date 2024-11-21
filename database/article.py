import wikipedia
import random

def get_random_article():
    """ Gets a random article from Wikipedia, its content, and linked articles.
    It returns a tuple containing the article's title, its content and a list of linked articles """
    while True: #Runs until it finds a valid article
        try:
            random_article_name = wikipedia.random() #Finds a random article and returns the name
            random_article = wikipedia.page(random_article_name) #Using the random article name, it returns the whole article 
            random_article_content = random_article.content #It gets the articles content
            random_article_links = random_article.links #It gets the articles links in a list 
        except wikipedia.exceptions.PageError: 
            print (f"PageError: Article '{random_article_name}' not found. Trying again...")
            continue 
        except wikipedia.exceptions.DisambiguationError as e:
            print (f"DisambiguationError: '{random_article_name}' is ambiguous." 
            f"Trying again with a different article...")
            continue 
        except Exception as e:
            print (f"Unexpected error: {e}. Retrying...")
            continue
        else:
            return random_article_name, random_article_content, random_article_links 
            #Returns a tuple, string, string, list

def get_specified_article(article_name):
    """ Gets a specified article depending on the article chosen by the user. """
    retries = 0
    set_of_tries = set()
    while retries < 15:
        try:
            article = wikipedia.page(article_name) #Gets the entire article using specified name (parameter)
            article_content = article.content #Gets articles content
            article_links = article.links #Gets the articles links
            return article, article_content, article_links #Returns a tuple.
        except wikipedia.exceptions.PageError:
            print (f"Article '{article_name}' not found")
            return None, None, None
        except wikipedia.exceptions.DisambiguationError as e:
            print (f"Trying again...")#
            set_of_tries.add(article_name)
            next_option = None 
            for option in e.options:
                if option not in set_of_tries:
                    next_option = option
                    break
            if next_option:
                article_name = next_option
                print("Trying with a different option...")
        except Exception as e:
            print (f"Unexpected error: {e}. Retrying...")
            continue
        retries += 1

# make indexes randomly in set
def set_random_links(article_links):
    """ Gets the links and randomly assigns them a number on the list.
    Returns a list. """
    list_of_numbers = list(range(1, len(article_links) + 1)) #Creates a list with numbers depending on the amount of links 
    random.shuffle(list_of_numbers) #Shuffles the numbers 
    set_of_links = set()  
    for number, link in zip(list_of_numbers, article_links):
        set_of_links.add(f"{number}.{link}") #Creates the pairs with no duplicates 
    sorted_links = sorted(set_of_links, key = lambda x: int(x.split('.')[0])) #organizes the items by number
    return sorted_links


    