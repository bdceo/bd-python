import csv
import codecs
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

    def gen_csv_row(self):
        return [self.name, self.rate, self.location, self.category, self.info_link, self.cover_link]


# 任务1:获取每个地区、每个类型页面的URL
def get_movie_url(category='喜剧', location='中国大陆'):
    base_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    if category.strip():
        base_url += ','+category.strip()
    if location.strip():
        base_url += ','+location.strip()
    return base_url


# 任务2: 获取电影页面 HTML
test_url = get_movie_url("爱情", "韩国")
test_html = expanddouban.get_html(test_url)


# 任务3: 定义电影类
movie_name = '肖生克的救赎'
movie_rate = 9.6
movie_location = '美国'
movie_category = '剧情'
movie_info_link = 'https://movie.douban.com/subject/1292052/'
movie_cover_link = 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
one_movie = Movie(movie_name, movie_rate, movie_location, movie_category, movie_info_link, movie_cover_link)


# 任务4: 获得豆瓣电影的信息
def get_movies(category, location):
    movie_url = get_movie_url(category, location);
    # print('抓取页面，url=', movie_url)
    movie_html = expanddouban.get_html(movie_url, True, 1)
    soup = BeautifulSoup(movie_html, 'html.parser')

    movies = []
    movie_html_list = soup.find(class_='list-wp').find_all('a', recursive=False)
    for item in movie_html_list:
        name = item.find(class_='title').string
        rate = item.find(class_='rate').string
        info_link = item.get('href')
        cover_link = item.find('img').get('src')
        # print(name, rate, location, category, info_link, cover_link)
        movies.append(Movie(name, rate, location, category, info_link, cover_link))
    return movies


# task4_list = get_movies('剧情', '美国')


# 任务5: 构造电影信息数据表
def get_all_location():
    # print('获取电影地区数据')
    location_list = []
    fetch_url = get_movie_url()
    fetch_html = expanddouban.get_html(fetch_url, False, 1)
    soup = BeautifulSoup(fetch_html, 'html.parser')
    location_html_list = soup.find_all(class_='category')
    for location_html in location_html_list:
        if '全部地区' in location_html.text:
            for li_html in location_html.find_all('li'):
                if '全部地区' not in li_html.text:
                    location_list.append(li_html.text)
    return location_list


def get_all_movie(cats, locates):
    movies = []
    for cat in cats:
        for loc in locates:
            movies.extend(get_movies(cat, loc))
    return movies


categories = ['剧情', '喜剧', '爱情']


def collect_movie():
    locations = get_all_location()
    movies = get_all_movie(categories, locations)
    # print("电影信息采集完毕.")

    with codecs.open('movies.csv', 'w', 'utf-8') as fo:
        csv_writer = csv.writer(fo)
        for mv in movies:
            csv_writer.writerow(mv.gen_csv_row())
        # print("已输出到csv.")


# 电影数据收集
# collect_movie()


# 任务6: 统计电影数据
with open('movies.csv', 'r') as fi:
    reader = csv.reader(fi)
    movie_list = list(reader)


def movie_stat():
    msgs = []
    for cat in categories:
        # print('统计电影分类：', cat)
        cat_stat = {}
        cat_locate_stat = {}
        # 每个分类及分类中地区电影统计
        for movie in movie_list:
            row_locate = movie[2]
            row_cat = movie[3]
            if cat == row_cat:
                if cat_stat.get(cat) is None:
                    cat_stat[cat] = 1
                else:
                    cat_stat[cat] += 1
                if cat_locate_stat.get(row_locate) is None:
                    cat_locate_stat[row_locate] = 1
                else:
                    cat_locate_stat[row_locate] += 1
        # print('分类统计结果：', cat_stat)
        # print('分类地区统计结果：', cat_locate_stat)

        locate_sort = sorted(cat_locate_stat.items(), key=lambda si: si[1], reverse=True)
        # print('电影数量前三名地区：', locate_sort[:3])

        msgs.append('{} 类电影共{}部，前三名地区如下：\n'.format(cat, cat_stat.get(cat)))
        for item in locate_sort[:3]:
            msgs.append('\t{}: {}部, 分类占比: {:.2%}\n'.format(*item, item[1]/cat_stat.get(cat)))

    return msgs


# 电影数据统计输出到文件
stat_msg = movie_stat()
with open('output.txt', 'a+', encoding='utf-8') as tf:
    for msg in stat_msg:
        tf.write(msg)

