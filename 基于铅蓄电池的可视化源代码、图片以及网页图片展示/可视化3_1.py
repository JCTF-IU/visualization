import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel文件
df = pd.read_excel('data of lead acid battery(1).xlsx')

# 初始化累积容量、电压和颜色的字典，以循环次数为键
cumulative_capacity = {}
voltages = {}
colors = {}

# 遍历数据，按循环次数分组处理
for cycle, data in df.groupby('循环'):
    cumulative_capacity[cycle] = []
    voltages[cycle] = []
    current_capacity = 0
    for index, row in data.iterrows():
        if row['充/放'] == 'CH':
            current_capacity += row['充电量(AH)']
        elif row['充/放'] == 'DIS':
            current_capacity -= row['放电量(AH)']
        cumulative_capacity[cycle].append(current_capacity)
        voltages[cycle].append(row['总电压(V)'])
        # 为每个循环指定一个颜色
    colors[cycle] = plt.cm.jet(cycle / df['循环'].max())

# 绘制累积容量的曲线
plt.figure(figsize=(10, 6))
for cycle in sorted(cumulative_capacity.keys()):
    plt.plot(cumulative_capacity[cycle], voltages[cycle], color=colors[cycle], label=f'Cycle {cycle}')

# 设置图表标题和坐标轴标签
plt.title('Cumulative Capacity Curve of Lead-Acid Battery')
plt.xlabel('Cumulative Capacity (AH)')
plt.ylabel('Total Voltage (V)')
plt.grid(True)  # 显示网格线

# 保存图片到当前目录
plt.savefig('cumulative_capacity_curve3_1.png', bbox_inches='tight')
plt.close()  # 关闭图表，释放资源
