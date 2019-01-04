
support_cities = ['chicago', 'new_york_city', 'washington']
city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
while city not in support_cities:
    print('Sorry! data not support your city:', city)
    city = input('Would you like to see data for Chicago, New York, or Washington?').lower()

print('get city: ',city)