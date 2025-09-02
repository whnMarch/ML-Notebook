import numpy as np
import matplotlib.pyplot as plt

# 定义 x 范围
x = np.linspace(-1, 5, 200)

# 方程组
# 2x - y = 0  -> y = 2x
y1 = 2 * x

# -x + 2y = 3 -> y = (x + 3) / 2
y2 = (x + 3) / 2

# 解方程组（矩阵法）
A = np.array([[2, -1],
              [-1, 2]])
b = np.array([0, 3])
solution = np.linalg.solve(A, b)
x_sol, y_sol = solution

# 绘制图像
plt.figure(figsize=(6,6))
plt.plot(x, y1, label=r"$2x - y = 0$")
plt.plot(x, y2, label=r"$-x + 2y = 3$")

# 标出解
plt.plot(x_sol, y_sol, 'ro', label=f"解: ({x_sol:.2f}, {y_sol:.2f})")

# 设置图形
plt.xlabel("x")
plt.ylabel("y")
plt.title("方程组的几何表示")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.show()
