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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

phone_dict = {}
for call in calls:
    tel_in, tel_out, tel_sec = call[0], call[1], call[3]
    if phone_dict.get(tel_in) is None:
        phone_dict[tel_in] = int(tel_sec)
    else:
        # phone_dict[tel_in] = int(phone_dict.get(tel_in)) + int(tel_sec)
        phone_dict[tel_in] += int(tel_sec)
    # if phone_dict.get(tel_out) is None:
    if tel_out not in phone_dict:
        phone_dict[tel_out] = int(tel_sec)
    else:
        # phone_dict[tel_out] = int(phone_dict.get(tel_out)) + int(tel_sec)
        phone_dict[tel_out] += int(tel_sec)

# 借助max函数，比sorted函数更简单
longest_call = max(zip(phone_dict.values(), phone_dict.keys()))
print('"<{}> spent the longest time, <{}> seconds, on the phone during\n September 2016.".'
      .format(*longest_call))

# 排序函数，指定key-排序字段，适用于字典数据类型
# phone_dict = sorted(phone_dict.items(), key=lambda item: item[1], reverse=True)
# print('"<{}> spent the longest time, <{}> seconds, on the phone during\n September 2016.".'
#      .format(longest_call[0], phone_dict[0][1]))


# 抽取函数处理，字典的初始化
def dict_add(adict, k, v):
    if k in adict:
        adict[k] += v
    else:
        adict[k] = v


test_dict = {}
for call in calls:
    dict_add(test_dict, call[0], int(call[3]))
    dict_add(test_dict, call[1], int(call[3]))
longest_call = max(test_dict, key=test_dict.get)
print(longest_call, test_dict[longest_call])
