# Numpy

[`Numpy`](https://numpy.org/)，是 **Python 中用于科学计算的核心库**之一，它提供了一个强大的​**多维数组对象（`ndarray`）**​，以及大量用于处理这些数组的函数。

- 多维数组对象；
- 丰富的数学函数；
- 科学计算基础；

---

## 如何使用

###1. 数组创建

```
arr1 = np.array([1, 2, 3])
arr2 = np.array((4, 5, 6))
print("从列表创建:", arr1)
print("从元组创建:", arr2)

zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
print("\n全 0 数组:\n", zeros)
print("全 1 数组:\n", ones)

empty = np.empty((2, 2))
print("\n空数组:\n", empty)

eye = np.eye(4)
print("\n4x4 单位矩阵:\n", eye)

range_arr = np.arange(1, 10, 2)  # [1,3,5,7,9]
print("\固定范围:", range_arr)

lin = np.linspace(0, 1, 5)  # [0,0.25,0.5,0.75,1]
print("等差数列:", lin)

rand = np.random.rand(2, 3)       # 均匀分布 [0,1)
randn = np.random.randn(2, 3)     # 标准正态分布
randint = np.random.randint(0, 10, (2, 3))  # 整数
print("\n随机均匀分布:\n", rand)
print("随机正态分布:\n", randn)
print("随机整数:\n", randint)
```

### 2. 基本属性

```
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\n数组形状 shape:", a.shape)
print("数组维度 ndim:", a.ndim)
print("数组元素个数 size:", a.size)
print("数组数据类型 dtype:", a.dtype)
print("数组元素大小 itemsize:", a.itemsize)
```

### 3. 数组运算

```
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print("\n加法:", x + y)
print("减法:", y - x)
print("乘法:", x * y)
print("除法:", y / x)
print("平方:", x ** 2)

# 广播
print("\n广播 (向量 + 标量):", x + 5)

# 统计函数
print("\n总和:", np.sum(y))
print("最小值:", np.min(y))
print("最大值:", np.max(y))
print("平均值:", np.mean(y))
print("中位数:", np.median(y))
print("标准差:", np.std(y))
print("方差:", np.var(y))

# 累积操作
print("\n累积和:", np.cumsum(x))
print("累积乘:", np.cumprod(x))
```

### 4. 矩阵运算

```
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("\n矩阵加法:\n", A + B)
print("矩阵减法:\n", A - B)
print("矩阵乘法 (元素乘):\n", A * B)
print("矩阵点乘 dot:\n", np.dot(A, B))
print("矩阵 @ 运算符:\n", A @ B)

# 转置
print("\n矩阵转置:\n", A.T)

# 逆矩阵（要求矩阵可逆）
inv_A = np.linalg.inv(A)
print("\n矩阵逆:\n", inv_A)

# 行列式
det_A = np.linalg.det(A)
print("矩阵行列式:", det_A)

# 特征值 & 特征向量
eigvals, eigvecs = np.linalg.eig(A)
print("特征值:", eigvals)
print("特征向量:\n", eigvecs)
```

### 5. 索引 & 切片

```
arr = np.arange(1, 11)
print("\n原数组:", arr)
print("切片 arr[2:5]:", arr[2:5])
print("倒序 arr[::-1]:", arr[::-1])

# 布尔索引
print("筛选大于 5 的元素:", arr[arr > 5])

# 花式索引
idx = [0, 2, 4, 6]
print("花式索引 arr[idx]:", arr[idx])
```

### 6. 重塑 & 拼接

```
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print("\n重塑为 3x4:\n", reshaped)

# 拼接
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6]])
print("\n上下拼接 vstack:\n", np.vstack((arr1, arr2)))
print("左右拼接 hstack:\n", np.hstack((arr1, arr2.T)))
```

### 7. 常用统计 & 随机

```
# 排序
arr = np.array([3, 1, 7, 2, 5])
print("\n排序:", np.sort(arr))
print("排序索引 argsort:", np.argsort(arr))

# 唯一值
print("唯一值 unique:", np.unique([1, 2, 2, 3, 4, 4, 5]))

# 随机打乱
arr = np.arange(10)
np.random.shuffle(arr)
print("随机打乱:", arr)
```

### 8. 索引

```
arr = np.arange(10, 100, 10)
print("花式索引 arr[[0,2,4]]:", arr[[0, 2, 4]])
matrix = np.arange(1, 13).reshape(3, 4)
print("二维花式索引 matrix[[0,2],[1,3]]:", matrix[[0, 2], [1, 3]])

arr = np.array([1, 3, 5, 7, 9])
mask = arr > 4
print("组合条件:", arr[(arr > 3) & (arr < 9)])
```

### 9. 高级切片

```
arr = np.arange(10)
sub = arr[2:6]
sub[0] = 99
print("\n切片返回视图 (修改子数组会影响原数组):", arr)

# 强制复制
sub_copy = arr[2:6].copy()
sub_copy[0] = -1
print("切片复制 (原数组不变):", arr)
```

### 10. 向量化运算

```
x = np.arange(5)
print("\n平方根:", np.sqrt(x))
print("指数:", np.exp(x))
print("对数:", np.log(x + 1))

# 自定义向量化函数
def my_func(x):
    return x**2 + 1

vec_func = np.vectorize(my_func)
print("自定义向量化函数:", vec_func(np.array([1, 2, 3, 4])))
```

### 11. 高级矩阵运算

```
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

print("\nKronecker 积:\n", np.kron(A, B))
print("Hadamard 逐元素乘:\n", np.multiply(A, B))
print("矩阵迹:", np.trace(A))

# 解线性方程组 Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print("线性方程组解 x:", x)
```

### 12. 内存共享与视图

```
arr = np.arange(6).reshape(2, 3)
reshaped = arr.reshape(3, 2)
reshaped[0, 0] = 999
print("\nreshape 默认共享内存:\n", arr)

reshaped_copy = arr.reshape(3, 2).copy()
reshaped_copy[0, 0] = -1
print("使用 copy() 避免修改原数组:\n", arr)
```

### 13. 高级随机数

```
rng = np.random.default_rng(42)

print("\n随机整数:", rng.integers(0, 10, size=5))
print("正态分布:", rng.normal(0, 1, 5))
print("随机抽样:", rng.choice([1, 2, 3, 4], size=2))
```

### 14. 掩码数组（Masked Array）

```
data = np.array([1, 2, -999, 4, 5])
masked = ma.masked_equal(data, -999)  # 把 -999 当作缺失值
print("\n掩码数组 (忽略缺失值求平均):", masked.mean())
```
