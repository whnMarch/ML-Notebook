# Pandas

[`Pandas`](https://pandas.pydata.org/)，专门用于 **数据分析和数据处理**.

- 数据读写：轻松地从各种文件格式（如 CSV, Excel, SQL 数据库, JSON）中读取数据，并写入其中。
- 数据清洗：处理缺失值、重复数据，以及进行数据格式转换。
- 数据筛选：基于条件快速筛选、排序和切片数据。
- 数据合并：像数据库中的 JOIN 操作一样，将不同的数据集按行或按列合并起来。
- 数据聚合：使用 groupby 功能对数据进行分组，并计算每组的统计信息（如总和、平均值等）。

---

## 第一章：pandas基础

### 一. 基本数据结构

#### 1. Series
由四个部分组成，分别是序列的值 data 、索引 index 、存储类型 dtype 、序列的名字 name

```
s = pd.Series(data = [100, 'a', {'dic1':5}],
              index = pd.Index(['id1', 20, 'third'], name='my_idx'),
              dtype = 'object',
              name = 'my_name')

print("values:", s.values)
print("index:", s.index)
print("dtype:", s.dtype)
print("name:", s.name)
print("shape 长度:", s.shape)
```
```
output:
    values: [100 'a' {'dic1': 5}]
    index: Index(['id1', 20, 'third'], dtype='object', name='my_idx')
    dtype: object
    name: my_name
    shape 长度: (3,)
```
#### 2. DataFrame
DataFrame 在 Series 的基础上增加了列索引，一个数据框可以由二维的 data 与行列索引来构造：

```
data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]
df = pd.DataFrame(data = data,
                  index = ['row_%d'%i for i in range(3)],
                  columns=['col_0', 'col_1', 'col_2'])

print("DataFrame:\n", df)
```
```
output:
    values: [100 'a' {'dic1': 5}]
    index: Index(['id1', 20, 'third'], dtype='object', name='my_idx')
    dtype: object
    name: my_name
    shape 长度: (3,)
```
用 [col_name] 与 [col_list] 来取出相应的
```
print("---------------------------------------------")
print("col_0:\n", df['col_0'])
print("---------------------------------------------")
print("col_0', 'col_1:\n", df[['col_0', 'col_1']])
```
```
---------------------------------------------
col_0:
 row_0    1
row_1    2
row_2    3
Name: col_0, dtype: int64
---------------------------------------------
col_0', 'col_1:
        col_0 col_1
row_0      1     a
row_1      2     b
row_2      3     c
```


### 二. 文件的读取和写入

#### 1. 文件的读取
```
df_csv = pd.read_csv('data/my_csv.csv')

output：
---------------------------------------------
df_csv:
       col1 col2  col3    col4      col5
0  0     2    a   1.4   apple  2020/1/1
1  1     3    b   3.4  banana  2020/1/2
2  2     6    c   2.5  orange  2020/1/5
3  3     5    d   3.2   lemon  2020/1/7

```


#### 2. 文件的写入
```
df_csv.to_csv('data/my_csv_saved.csv', index=False)
```


### 三. 常用基本函数

#### 1. 汇总函数
head, tail 函数分别表示返回表或者序列的前 n 行和后 n 行，其中 n 默认为5：

```
file_path = os.path.join(script_dir, 'data', 'student_data.csv')
df = pd.read_csv(file_path)
print("---------------------------------------------")
print("head:\n", df.head(2))
print("tail:\n", df.tail(3))
```
```
output:
---------------------------------------------
head:
                    School   Grade           Name  Gender  Height  Weight Transfer
0  Sun Yat-sen University  Junior  Xiaohua Zhang  Female   174.2    68.9        Y
1     Zhejiang University  Senior     Haoran Sun  Female   151.3    41.9        N
tail:
                   School      Grade         Name  Gender  Height  Weight Transfer
997  Tsinghua University  Sophomore  Xiaohua You    Male   165.7    47.5        N
998     Fudan University   Freshman  Zhenyu Chen    Male   162.1    87.8        N
999     Fudan University  Sophomore   Zhenyu Sun  Female   167.3    87.4        Y
```
最常见的是 sum, mean, median, var, std, max, min
```
df_demo = df[['Height', 'Weight']]
print("---------------------------------------------")
print("mean:\n", df_demo.mean())
print("max:\n", df_demo.max())

✳ 0：会计算每一列的平均值 ；1：计算每一行的平均值
print("axis=0:\n", df_demo.mean(axis=0).head())
print("axis=1:\n", df_demo.mean(axis=1).head())

```
```
output:
---------------------------------------------
mean:
 Height    169.8137
Weight     65.2303
dtype: float64
max:
 Height    190.0
Weight     89.9
dtype: float64
---------------------------------------------
axis=0:
 Height    169.8137
Weight     65.2303
dtype: float64
axis=1:
 0    121.55
1     96.60
2    116.15
3    115.65
4    117.20
```

quantile, count, idxmax 这三个函数，分位数、非缺失值个数、最大值对应的索引：
```
print("---------------------------------------------")
print("quantile:\n", df_demo.quantile(0.75))
print("count:\n", df_demo.count())
print("idxmax:\n", df_demo.idxmax())
```
```
output:
---------------------------------------------
quantile:
 Height    180.400
Weight     77.625
Name: 0.75, dtype: float64
count:
 Height    1000
Weight    1000
dtype: int64
idxmax:
 Height    206
Weight     28
dtype: int64
```

unique 和 nunique 可以分别得到其唯一值组成的列表和唯一值的个数

unique：列出所有不同的学校名称；nunique：计算不同学校的总数；
```
print("---------------------------------------------")
print("quantile:\n", df_demo.quantile(0.75))
print("count:\n", df_demo.count())
print("idxmax:\n", df_demo.idxmax())
```

```
output:
---------------------------------------------
unique:
 ['Sun Yat-sen University' 'Zhejiang University' 'Nanjing University'
 'Tongji University' 'Shanghai Jiao Tong University' 'Tsinghua University'
 'Fudan University' 'Peking University']
nunique:
 8
```

