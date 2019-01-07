
name = 'bdceo'
age = 30
print ('My name is ', name, ' and ', age, 'years old.')

# gf = input('tell me your gf name: ')
# print ('Hello:', gf)

print('1024*768=', 1024 * 768)

# 元组，将相关信息存到一个容器中，例如：经纬度，xyz
location = (1233.21, 32111.2)
location2 = 1233.21, 32111.2
print('lat={}, lan={}'.format(location[0], location[1]))
print(location == location2)
# 可以不用括号，并同时赋值给三个变量
xyz = 1, 2, 3
x, y, z = xyz
print('x={}, y={}, z={}'.format(x, y, z))

# 集合 set， 无序，不重复，可变
nums = [2, 3, 4, 2, 1, 3, 1, 4, 5, 6, 7, 3, 2, 1, 1]
print(nums)
num_set = set(nums)
print('num_set=', num_set, ' size=', len(num_set))
print('7 in num_set: {}'.format(7 in num_set))
print(num_set.pop())
num_set2 = {4, 5, 9, 11}
print('num_set2=', num_set2)
print('union=', num_set.union(num_set2))
print('intersection 交集=', num_set.intersection(num_set2))
print('difference 差集=', num_set.difference(num_set2))

# 字典
person = {'age':28, 'name':'bdceo', 'sanwei':(12,23,34)}
print('person=', person)
print('name=', person['name'])
print('age=', person.get('age'))
print('sanwei in person =', 'sanwei' in person)
# print('sal=', person['sal']) 会返回KeyError错误，get方法只会返回None，或者返回指定的默认值
print('sal=', person.get('sal'))
print('sal default=', person.get('sal', '28'))
print('sal is None=', person.get('sal') is None)
print('age is not None=', person.get('age') is not None)
print('person=', person)

# 列表 a 和列表 b 是对等和相同的。列表 c 等同于 a（因此等同于 b），因为它们具有相同的内容。但是 a 和 c（同样 b 也是）指向两个不同的对象，即它们不是相同的对象。这就是检查是否相等与恒等的区别。
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print('a==b ', a == b)
print('a is b ', a is b)
print('a==c ', a == c)
print('a is c ', a is c)

name = 'Chenye Ding'
print(name.lower())

# max 取map中的最大值，按k或v排序
# 先zip 将kv对组成元组，然后取最大

calls = {'134':253, '189':103, '152':80}
print(calls)
print(calls.keys())
print(calls.values())
for k,v in zip(calls.keys(), calls.values()):
    print('{}>>{}'.format(k, v))
order_by_k = max(zip(calls.keys(), calls.values()))
print('max of k={}>>{}'.format(*order_by_k))

for v,k in zip(calls.values(), calls.keys()):
    print('{}>>{}'.format(v, k))
order_by_v = max(zip(calls.values(), calls.keys()))
print('max of v={}>>{}'.format(*order_by_v))

