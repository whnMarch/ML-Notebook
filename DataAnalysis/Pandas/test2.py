import os
import numpy as np
import pandas as pd

# ====================================
# 二. 数据处理
# ====================================

# 1. 索引器
s = pd.Series([1, 2, 3, 4, 5, 6],
               index=['a', 'b', 'a', 'a', 'a', 'c'])

# print("---------------------------------------------")
# print("s['a']：\n", s['a'])
# print("s[['c', 'b']]：\n", s[['c', 'b']])
# print("s['c': 'b': -2]：\n", s['c': 'b': -2])
# print("s.sort_index()['a': 'b']：\n", s.sort_index()['a': 'b'])


# 2. loc索引器（ 元素 ）
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data', 'student_data.csv')
df = pd.read_csv(file_path)
df.set_index('Name', inplace=True) 

print("df.loc['Qiang Sun']：\n", df.loc['Qiang Sun'])
print("df.loc['Qiang Sun', 'School']：\n", df.loc['Qiang Sun', 'School'])
names = ['Qiang Sun', 'Quan Zhao']
existing_names = [name for name in names if name in df.index]
print("存在的名字：", existing_names)
print("结果：\n", df.loc[existing_names, ['School', 'Gender']])

# 3. iloc索引器（ 位置 ）


# 4. Query方法
q_df = df.query('((School == "Fudan University")&'
         ' (Grade == "Senior")&'
         ' (Weight > 70))|'
         '((School == "Peking University")&'
         ' (Grade != "Senior")&'
         ' (Weight > 80))')

print("---------------------------------------------")
print("q_df:\n", q_df)

# 5.随机抽样
df_sample = pd.DataFrame({'id': list('abcde'),
                          'value': [1, 2, 3, 4, 90]})


print("df_sample：\n", df_sample)
df_result = df_sample.sample(3, replace = True, weights = df_sample.value)
print("---------------------------------------------")
print("df_result:\n", df_result)