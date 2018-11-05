# 文件读写
import random as rd

f = open("D:/udacity/python/first-script.py")
data = f.read()
# print(data)
f.close()

# with 开头语法，执行完代码块，文件自动关闭
lines = []
with open('D:/udacity/python/first-script.py') as f:
    line = f.readline()
    print('first line:', line)
    for line in f:
        lines.append(line)
# print(lines)
print(rd.choice(lines))
print(rd.sample(lines,2))