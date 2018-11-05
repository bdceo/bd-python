
# 流程控制，if，while，for

altitude = 10000
speed = 250
propulsion = "Propeller"
res = (altitude > 500 and speed > 100) or not propulsion == "Propeller"
print(res)
print((altitude > 500 and speed > 100))

# rang函数，生成不可变的数字序列，返回是range对象，可以强转成list对象打印输出，或用于循环中
rgs = [1, 2]
print(type(rgs))
rgs = list(range(10))
print(rgs)
rgs = list(range(3, 10))
print(rgs)
rgs = list(range(2, 10, 3))
print(rgs)

# zip，可以将两个列表同时迭代循环，也可以将一对元组数据，解压缩到两个列表中
# 组合 和 拆分 列表
names = ['coo', 'cto', 'ceo']
ages = [12, 34, 22]
for name, age in zip(names, ages):
    print("{} - {}".format(name, age))
zips = [('coo',12),('cto', 42),('ceo', 44)]
unames , uages = zip(*zips)
print(unames)
print(uages)

#enumerate ，返回迭代元组对象（i, item）
for i, name in enumerate(names):
    print('{}={}'.format(i, name))

# 快速创建列表

name_list = [ name.title() for name in names ]
print(name_list)
sqrs = [i**2 for i in range(10) if i%2 == 0]
print(sqrs)

# 提取名字
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split()[0].lower() for name in names]
print(first_names)

# 3 的倍数
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

# 按得分过滤姓名
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name, score in scores.items() if score >= 65]
print(passed)