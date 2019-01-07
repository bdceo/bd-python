import pandas as pd

# 测试循环接收客户端输入
support_cities = ['chicago', 'new_york_city', 'washington']
city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
while city not in support_cities:
    print('Sorry! data not support your city:', city)
    city = input('Would you like to see data for Chicago, New York, or Washington?').lower()

print('get city: ', city)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

print(CITY_DATA.get(city))

df = pd.read_csv(CITY_DATA.get(city))
print(df.info())


month = 'march'
months = ['january', 'february', 'march', 'april', 'may', 'june']
print(months.index(month) + 1)


