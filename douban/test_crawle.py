import time
import urllib
import requests
from bs4 import BeautifulSoup


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("search the target url")
        return False
    elif len(search_history) >= max_steps:
        print('search history has', max_steps)
        return False
    # elif len(search_history) > len(set(search_history)):
    elif search_history[-1] in search_history[:-1]:
        print('search history has loop')
        return False
    else:
        print('continue search')
        return True

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

article_chain = [start_url]


def find_first_link(url):
    print('find the first link in url:', url)
    # get the HTML from "url", use the requests library
    response = requests.get(url)
    html = response.text

    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # find the first link in the article
    first_link = None
    all_p = soup.find(id='mw-content-text').find(class_='mw-parser-output').find_all('p', recursive=False)
    for p in all_p:
        p_a = p.find('a', recursive=False)
        if p_a is not None:
            first_link = p_a.get('href')
            break
    if not first_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)
    print(first_link)

    # return the first link as a string, or return None if there is no link
    return first_link


while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])

    if not first_link:
        print("We're arrived at an article with no links, aborting search!")
        break

    # add the first link to article_chain
    article_chain.append(first_link)

    # delay for about two seconds
    time.sleep(2)

