import requests
from bs4 import BeautifulSoup

# TODO: Implement the continue_crawl function described above
def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("search the target url")
        return False
    elif len(search_history) >= max_steps:
        print('search history has 25')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('search history has loop of 1')
        return False
    elif len(search_history) > len(set(search_history)):
        print('search history has loop of 2')
        return False
    else:
        print('continue search')
        return True


article_chain = ['https://en.wikipedia.org/wiki/Floating_point',
           'https://en.wikipedia.org/wiki/Computing',
           'https://en.wikipedia.org/wiki/Computer',
           'https://en.wikipedia.org/wiki/Arithmetic',
           'https://en.wikipedia.org/wiki/Boolean_algebra',
           'https://en.wikipedia.org/wiki/Mathematics',
           'https://en.wikipedia.org/wiki/Pattern',
           'https://en.wikipedia.org/wiki/Arithmetic']

target_url = 'https://en.wikipedia.org/wiki/Pattern'

continue_crawl(article_chain, target_url)


while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    html = requests.get(article_chain[-1])

    # find the fist a



