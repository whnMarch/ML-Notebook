import os
import numpy as np
import pandas as pd

# ====================================
# 一. 基本数据结构
# ====================================

# 1. Series
s = pd.Series(data = [100, 'a', {'dic1':5}],
              index = pd.Index(['id1', 20, 'third'], name='my_idx'),
              dtype = 'object',
              name = 'my_name')

print("values:", s.values)
print("index:", s.index)
print("dtype:", s.dtype)
print("name:", s.name)
print("shape 长度:", s.shape)

# 2. DataFrame
data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]
df = pd.DataFrame(data = data,
                  index = ['row_%d'%i for i in range(3)],
                  columns=['col_0', 'col_1', 'col_2'])

print("DataFrame:\n", df)
print("---------------------------------------------")
print("col_0:\n", df['col_0'])
print("---------------------------------------------")
print("col_0', 'col_1:\n", df[['col_0', 'col_1']])


# ====================================
# 二. 文件的读取和写入
# ====================================
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data', 'my_csv.csv')

# 1. 文件的读取
print("---------------------------------------------")
df_csv = pd.read_csv(file_path)
print("df_csv:\n", df_csv)


# 2. 文件的写入
# df_csv.to_csv('data/my_csv_saved.csv', index=False)

# ====================================
# 三. 常用基本函数
# ====================================

file_path = os.path.join(script_dir, 'data', 'student_data.csv')
df = pd.read_csv(file_path)
print("---------------------------------------------")
print("head:\n", df.head(2))
print("tail:\n", df.tail(3))

df_demo = df[['Height', 'Weight']]
print("---------------------------------------------")
print("mean:\n", df_demo.mean())
print("max:\n", df_demo.max())
print("---------------------------------------------")
print("axis=0:\n", df_demo.mean(axis=0).head())
print("axis=1:\n", df_demo.mean(axis=1).head())


print("---------------------------------------------")
print("quantile:\n", df_demo.quantile(0.75))
print("count:\n", df_demo.count())
print("idxmax:\n", df_demo.idxmax())

print("---------------------------------------------")
print("unique:\n", df['School'].unique())
print("nunique:\n", df['School'].nunique()) 