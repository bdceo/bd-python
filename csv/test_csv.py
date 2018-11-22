import csv
import codecs


# 电影类
class Movie(object):

    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def csv(self):
        return [self.name, self.rate, self.location, self.category, self.info_link, self.cover_link]


movie_name = '肖生克的救赎'
movie_rate = 9.6
movie_location = '美国'
movie_category = '剧情'
movie_info_link = 'https://movie.douban.com/subject/1292052/'
movie_cover_link = 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg'
movie = Movie(movie_name, movie_rate, movie_location, movie_category, movie_info_link, movie_cover_link)


# 写入csv
# with codecs.open('out.csv', 'w', 'utf-8') as f:
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(movie.csv())

print("csv gen finish.")


