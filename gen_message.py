'''
练习：生成消息
假设你是一名老师，需要向每位学生发一条消息，提醒他们未交的作业和分数是多少。你知道每名学生的姓名，没交的作业份数和分数，这些数据保存在了电子表格中，你只需将这些输入插入你想到的以下消息中即可：

Hi [insert student name],

This is a reminder that you have [insert number of missing assignments] assignments left to submit before you can graduate. Your current grade is [insert current grade] and can increase to [insert potential grade] if you submit all assignments before the due date.

你可以将此消息复制粘贴后发送给每位学生，并且每次手动插入相应的值。但是你要写一个程序来帮助你完成这一流程。

写一个完成以下操作的脚本：

请求用户输入三次。一次是名字列表，一次是未交作业数量列表，一次是分数列表。使用该输入创建 names、assignments 和 grades 列表。
使用循环为每个学生输出一条信息并包含正确的值。潜在分数是 2 乘以未交作业数加上当前分数。
'''

names = input('names:').title().split(',')
counts = input('counts:').title().split(',')
grades = input('grades:').title().split(',')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for i, name in enumerate(names):
    print(message.format(name, counts[i], grades[i], int(grades[i]) + int(counts[i])*2))

for name, count, grade in zip(names, counts, grades):
    print(message.format(name, count, grade, int(grade) + int(count) * 2))
