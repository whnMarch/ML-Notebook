
## 第二章：数据处理

### 一. 索引

#### 1. 索引器
```
s = pd.Series([1, 2, 3, 4, 5, 6],
               index=['a', 'b', 'a', 'a', 'a', 'c'])

print("---------------------------------------------")
print("s['a']：\n", s['a']) 
print("s[['c', 'b']]：\n", s[['c', 'b']])
#-2 表示步长为 -2，即从后往前每隔一个元素取一个。
print("s['c': 'b': -2]：\n", s['c': 'b': -2])
#s.sort_index() 会按字母顺序对索引进行排序，将所有 'a' 标签的元素排在一起，然后是 'b'，最后是 'c'。

#['a': 'b'] 再进行切片，就能得到从 'a' 到 'b' 标签之间的所有元素。
print("s.sort_index()['a': 'b']：\n", s.sort_index()['a': 'b'])
```

```
---------------------------------------------
s['a']：
 a    1
a    3
a    4
a    5
dtype: int64
s[['c', 'b']]：
 c    6
b    2
dtype: int64
s['c': 'b': -2]：
 c    6
a    4
b    2
dtype: int64
s.sort_index()['a': 'b']：
 a    1
a    3
a    4
a    5
b    2
dtype: int64
```

#### 2. loc索引器（ 元素 ）
使用 loc 就像你对表格说：“给我把名字叫 '张三' 的那一行和列名叫 '年龄' 的那几列找出来。

* 选择方式
  * 选择单行和单列： df.loc['苹果', '颜色'] → '红色'
  * 选择多行和多列： df.loc[['苹果', '西瓜'], ['颜色', '价格']]
  * 切片选择（包含终点）： df.loc['苹果':'西瓜', '价格'],这将返回从苹果到西瓜（包括西瓜）这两行的价格数据。
```
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data', 'student_data.csv')
df = pd.read_csv(file_path)
df.set_index('Name', inplace=True) 
```
```
Qiang Sun         Sun Yat-sen University     Junior  Female   151.7    77.0        Y
Qiang Sun               Fudan University     Junior    Male   154.4    52.5        Y
```

同时选择行和列
```
print("df.loc['Qiang Sun', 'School']：\n", df.loc['Qiang Sun', 'School'])
```
```
Qiang Sun           Sun Yat-sen University
Qiang Sun                 Fudan University
Qiang Sun                Tongji University
```
取出列表中所有元素值对应的行或列
```
names = ['Qiang Sun', 'Quan Zhao']
existing_names = [name for name in names if name in df.index]
print("存在的名字：", existing_names)
print("结果：\n", df.loc[existing_names, ['School', 'Gender']])
```
```
                                   School  Gender
Name
Qiang Sun         Sun Yat-sen University  Female
Qiang Sun               Fudan University    Male
Qiang Sun              Tongji University  Female
Qiang Sun             Nanjing University  Female
```

#### 3. iloc索引器（ 位置 ）
使用整数位置来选择数据。行和列的索引都从 0 开始。

* 选择方式
  * 选择单行和单列： df.iloc[0, 0] → '红色' （第 0 行，第 0 列）
  * 选择多行和多列： df.iloc[[0, 2], [0, 1]]
  * 切片选择（不包含终点）： df.iloc[0:2, 1]这将返回第 0 行到第 2 行（不包括第 2 行）的第 1 列数据，即苹果和香蕉的价格。




#### 4. Query方法
执行结果返回布尔列表, Transfer列

```
q_df = df.query('((School == "Fudan University")&'
         ' (Grade == "Senior")&'
         ' (Weight > 70))|'
         '((School == "Peking University")&'
         ' (Grade != "Senior")&'
         ' (Weight > 80))')

print("---------------------------------------------")
print("q_df:\n", q_df)
```
```
                              School      Grade  Gender  Height  Weight Transfer
Name
Yuchen Zhou        Fudan University     Senior  Female   155.8    83.5        Y
Qiang Wang        Peking University     Junior  Female   152.2    89.9        Y
Zhenyu Wang        Fudan University     Senior    Male   179.2    76.8        Y
Liwei You         Peking University  Sophomore    Male   169.9    83.7        Y
Zhenyu Chen       Peking University  Sophomore  Female   161.5    80.3        N
```

#### 5.随机抽样
ample 函数中的主要参数为 n, axis, frac, replace, weights ，前三个分别是指抽样数量、抽样的方向（0为行、1为列）和抽样比例（0.3则为从总体中抽出30%的样本）。

replace 和 weights 分别是指是否放回和每个样本的抽样相对概率，当 replace = True 则表示有放回抽样。

```
df_sample = pd.DataFrame({'id': list('abcde'),
                          'value': [1, 2, 3, 4, 90]})


print("df_sample：\n", df_sample)
df_result = df_sample.sample(3, replace = True, weights = df_sample.value)
print("---------------------------------------------")
print("df_result:\n", df_result)
```

```
   id  value
0  a      1
1  b      2
2  c      3
3  d      4
4  e     90
---------------------------------------------
df_result:
   id  value
4  e     90
4  e     90
4  e     90
```