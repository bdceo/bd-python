
# 多变量同时赋值
a, b, c = 1, 2, 3
print('a=', a, ', b=', b, ', c=', c)


age = 30
is_cn = (age>=18 and age<60)
is_yon = not (age>=18 and age<60)
print(is_cn)
print(is_yon)

# 字符串包含， 列表包含  in, not in

si = 'bdceo' in 'my name is bdceo'

lis = [1, 3, 4, 6, 7]
li5 = 5 in lis
li3 = 3 not in lis
print(si, li5, li3)

# 字符串 连接方法：join
num_str = '#'.join(['bdceo','bdcoo','bdcfo'])
print('join strs:', num_str)

# 列表方法： len，max，min，append
lis.append(9)
print(lis)
print('add 9 to lis', ', size=', len(lis), ', max=',  max(lis), ', min=', min(lis))
lis_sort = sorted(lis)
print('sorted lis', lis_sort)

ai = [1,2,3]
bi = [4,5,6]
print(ai)
print(bi)
result_1 = ai.append(bi)
result_2 = ai + bi
print(result_1)
print(result_2)



