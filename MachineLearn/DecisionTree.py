import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. 准备数据
# 假设我们有以下数据来决定是否“去打球”
# 特征 (X): [天气, 温度, 湿度, 风力]
# 为了简化，我们将文本特征转换为数字：
# 天气: 晴天=2, 阴天=1, 雨天=0
# 温度: 炎热=2, 温和=1, 凉爽=0
# 湿度: 高=1, 正常=0
# 风力: 强=1, 弱=0

# 训练数据特征
# 每行代表一个样本
X_train = np.array([
    [2, 2, 1, 0],  # 晴天, 炎热, 高湿, 无风 -> 不去
    [2, 2, 1, 1],  # 晴天, 炎热, 高湿, 有风 -> 不去
    [2, 0, 0, 1],  # 晴天, 凉爽, 正常, 有风 -> 去
    [1, 2, 1, 0],  # 阴天, 炎热, 高湿, 无风 -> 去
    [0, 1, 1, 0],  # 雨天, 温和, 高湿, 无风 -> 去
    [0, 0, 0, 0],  # 雨天, 凉爽, 正常, 无风 -> 去
    [0, 0, 0, 1],  # 雨天, 凉爽, 正常, 有风 -> 不去
    [1, 0, 0, 1]   # 阴天, 凉爽, 正常, 有风 -> 去
])

# 训练数据标签 (y)
# 1 代表 "去打球", 0 代表 "不去打球"
y_train = np.array([0, 0, 1, 1, 1, 1, 0, 1])

# 特征和类别的名称（用于可视化）
feature_names = ['Weather', 'Temperature', 'Humidity', 'Wind']
class_names = ['Not Play', 'Play']


# 2. 创建并训练模型
# 创建一个决策树分类器实例
# random_state=42 保证每次运行结果都一样，便于复现
model = DecisionTreeClassifier(criterion='entropy', random_state=42)

# 使用训练数据来训练模型
model.fit(X_train, y_train)

print("✅ 决策树模型训练完成!")


# 3. 进行预测
# 假设今天的天气是：[天气=晴天(2), 温度=温和(1), 湿度=高(1), 风力=无风(0)]
new_data = np.array([[2, 1, 1, 0]])

# 使用训练好的模型进行预测
prediction = model.predict(new_data)
prediction_proba = model.predict_proba(new_data)

print(f"\n🤔 新数据: {new_data[0]}")
print(f"🎯 预测结果: {class_names[prediction[0]]} (原始值: {prediction[0]})")
print(f"📊 预测概率 [不去, 去]: {prediction_proba[0]}")


# 4. 可视化决策树
# 创建一个图形来展示决策树
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    filled=True, # 用颜色填充节点
    feature_names=feature_names,
    class_names=class_names,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree for Playing Tennis")
plt.show()