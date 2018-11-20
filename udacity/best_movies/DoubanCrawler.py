import requests
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
def get_movie_url(category, location):
    base_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    if category.strip():
        base_url += ','+category.strip()
    if location.strip():
        base_url += ','+location.strip()
    return base_url


# 任务2: 获取电影页面 HTML
movie_url = get_movie_url("剧情", "美国")
# movie_html = expanddouban.get_html(movie_url, True)


# 任务3: 定义电影类
movie_name = '肖生克的救赎'
movie_rate = 9.6
movie_location = '美国'
movie_category = '剧情'
movie_info_link = 'https://movie.douban.com/subject/1292052/'
movie_cover_link = 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
movie = Movie(movie_name, movie_rate, movie_location, movie_category, movie_info_link, movie_cover_link)


# 任务4: 获得豆瓣电影的信息




# 任务5: 构造电影信息数据表

# 任务6: 统计电影数据



