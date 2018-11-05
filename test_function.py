# 函数

def cylinder_volume(h, r=3):
    p = 3.14159
    return h * p * r *2

print(cylinder_volume(13, 5))
print(cylinder_volume(13))
print(cylinder_volume(r=13, h=6))

egg_count = 0

def buy_eggs():
    # egg_count += 12 # python不允许在函数内修改外部变量的值
    return egg_count+12
buy_eggs()

# 内置函数：map—— 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# map(function, iterable, ...)
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
def mean(num_list):
    return sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
print(averages)

def sqre(x):
    return x ** 2
print(list( map(sqre, [1, 3, 5]) ))
print(list( map(lambda x: x ** 2, [1, 3, 5]) ))
print(list( map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6]) ))

# 内置函数：list——将元组转换为列表。

# 内置函数：filter——函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中
# filter(function, iterable)
def gt10(x):
    return x>10
print(list( filter(gt10, [2, 3, 5, 12, 42, 31, 10]) ))
print(list( filter(lambda x: x>10, [2, 3, 5, 12, 42, 16, 10]) ))

# 迭代器，生成器
# yield 关键词，使得函数可以生成多个返回值，成为生成器
def my_range(x):
    i = 0
    while i<x :
        yield i
        i += 1
print(list(my_range(5)))

print(range(25))

# 如果可迭代对象太大，无法完整地存储在内存中（例如处理大型文件时），每次能够使用一部分很有用。
# 实现一个生成器函数 chunker，接受一个可迭代对象并每次生成指定大小的部分数据。
def chunker(iterable, size):
    i=0
    tmp = []
    t = len(iterable)
    for item in iterable:
        tmp.append(item)
        i += 1
        if i%size==0 or i==t:
            yield tmp
            tmp = []

def chunker2(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i: i+size]

for chunk in chunker2(range(25), 4):
    print(list(chunk))
for chunk in chunker2('python programming', 5):
    print(list(chunk))
