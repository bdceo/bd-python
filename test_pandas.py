# 导入 pandas ，numpy 库
import pandas as pd
import numpy as np

# 创建 Series
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print(groceries)
# 输出形状，维数，数据大小
print('groceries.shape=', groceries.shape)
print('groceries.ndim=', groceries.ndim)
print('groceries.size=', groceries.size)
# 输出内容和索引
print('groceries.values=', groceries.values)
print('groceries.index=', groceries.index)
# 检查索引是否存在
print('orange in groceries: ', 'orange' in groceries)
print('apples in groceries: ', 'apples' in groceries)