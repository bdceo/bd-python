import csv
import requests
from bs4 import BeautifulSoup
import expanddouban


# 电影类
class Movie(object):

    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


# 任务1:获取每个地区、每个类型页面的URL
def get_movie_url(category='喜剧', location='中国大陆'):
    base_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    if category.strip():
        base_url += ','+category.strip()
    if location.strip():
        base_url += ','+location.strip()
    return base_url


# 任务2: 获取电影页面 HTML
test_url = get_movie_url("剧情", "美国")
# test_html = expanddouban.get_html(test_url)


# 任务3: 定义电影类
movie_name = '肖生克的救赎'
movie_rate = 9.6
movie_location = '美国'
movie_category = '剧情'
movie_info_link = 'https://movie.douban.com/subject/1292052/'
movie_cover_link = 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
movie = Movie(movie_name, movie_rate, movie_location, movie_category, movie_info_link, movie_cover_link)


# 任务4: 获得豆瓣电影的信息
def get_movies(category='剧情', location='美国'):
    movie_url = get_movie_url(category, location);
    print('抓取电影页面，url=', movie_url)
    movie_html = expanddouban.get_html(movie_url, True)
    soup = BeautifulSoup(movie_html, 'html.parser')

    movies = []
    movie_html_list = soup.find(class_='list-wp').find_all('a', recursive=False)
    for item in movie_html_list:
        name = item.find(class_='title').string
        rate = item.find(class_='rate').string
        info_link = item.get('href')
        cover_link = item.find('img').get('src')
        print(name, rate, location, category, info_link, cover_link)
        movies.append(Movie(name, rate, location, category, info_link, cover_link))
    return movies
# movie_list = get_movies()


# 任务5: 构造电影信息数据表
def get_all_location():
    location_list = []
    fetch_url = get_movie_url()
    fetch_html = expanddouban.get_html(fetch_url, False)
    soup = BeautifulSoup(fetch_html, 'html.parser')
    location_html_list = soup.find_all(class_='category')
    for location_html in location_html_list:
        if '全部地区' in location_html.text:
            for li_html in location_html.find_all('li'):
                if '全部地区' not in li_html.text:
                    location_list.append(li_html.text)
    return location_list


def get_all_movie(cats, locs):
    movie_list = []
    for cat in cats:
        for loc in locs:
            movie_list.append(get_movies(cat, loc))
    return movie_list


# 三个类型：剧情，喜剧，动作
categories = ['剧情', '喜剧', '动作']
# 所有地区
locations = get_all_location()
# 所有电影
movie_data = get_all_movie(categories, locations)
print(movie_data)
print ("movie fetch finish.")
# 写入csv
out = open('movies.csv', 'a', newline='')
csv_writer = csv.writer(out, dialect='excel')
for movie in movie_data:
    csv_writer.writerow(movie)
print("csv gen finish.")


# 任务6: 统计电影数据



