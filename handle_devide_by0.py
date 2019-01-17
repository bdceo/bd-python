'''
练习：处理除以零的情形
现在运行下面的代码将在第二次调用 handle_zero 函数时导致错误，因为它遇到了 ZeroDivisionError 异常。

请修改下面的函数以处理该异常。如果在函数的第一行遇到该异常，应该输出警告消息并返回空列表。否则，应该运行函数的剩余代码。最后，该函数应该始终输出返回了多少组。
'''

# range 函数参考：http://www.runoob.com/python/python-func-range.html
# range(start, stop[, step])


def create_groups(items, num_groups):
    groups = []
    try:
        size = len(items) // num_groups
    except ZeroDivisionError as e:
        print('WARNING: Returning empty list. Please use a nonzero number.')
        print('WARNING: {}'.format(e))
        return groups
    else:
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(num_groups))


print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))