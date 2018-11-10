"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

diff_phones = set()
for text in texts:
    diff_phones.add(text[0])
    diff_phones.add(text[1])
for call in calls:
    diff_phones.add(call[0])
    diff_phones.add(call[1])

print('"There are <{}> different telephone numbers in the records."'.format(len(diff_phones)))

# 将一行3列的列表，解压缩到三个元组
texts_transposed = list(zip(*texts))
for tt in texts_transposed:
    print(tt)
print('-----')
calls_transposed = list(zip(*calls))
for cc in calls_transposed:
    print(cc)
size = len(set(texts_transposed[0]) | set(texts_transposed[1]) | set(calls_transposed[0]) | set(calls_transposed[1]))
print(size)
