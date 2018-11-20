import requests
import expanddouban

# 任务1:获取每个地区、每个类型页面的URL
def getMovieUrl(category, location):
    url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    if category.strip():
        url += ','+category.strip()
    if location.strip():
        url += ','+location.strip()
    return url


# 任务2: 获取电影页面 HTML
url = getMovieUrl("枪战","美国")
html = expanddouban.getHtml(url)

# 任务3: 定义电影类

# 任务4: 获得豆瓣电影的信息

# 任务5: 构造电影信息数据表

# 任务6: 统计电影数据



