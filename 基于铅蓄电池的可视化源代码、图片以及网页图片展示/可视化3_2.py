import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的工作表
df = pd.read_excel('data of lead acid battery(1).xlsx')

# 初始化累计容量
cumulative_capacity = 0
processed_data = []  # 初始化processed_data列表，用于存储处理后的数据

# 处理数据，只保留总电压、充电量、放电量和循环次数，并计算累计容量
first_charge_found = False
for index, row in df.iterrows():
    charge_amount = row['充电量(AH)']
    discharge_amount = row['放电量(AH)']
    total_voltage = row['总电压(V)']
    cycle = row['循环']

    if pd.notnull(charge_amount) and charge_amount > 0:
        cumulative_capacity += charge_amount
        first_charge_found = True
    elif pd.notnull(discharge_amount) and discharge_amount > 0:
        cumulative_capacity -= discharge_amount

    if first_charge_found:
        processed_data.append((cumulative_capacity, total_voltage, cycle))

    # 将处理后的数据转换为DataFrame
processed_df = pd.DataFrame(processed_data, columns=['累计容量(AH)', '总电压(V)', '循环'])

# 绘制图表，使用循环次数作为不同的线
plt.figure(figsize=(10, 6))
for cycle, group in processed_df.groupby('循环'):
    plt.plot(group['累计容量(AH)'], group['总电压(V)'], label=f'Cycle {cycle}', marker='o', markersize=3, linestyle='-',
             linewidth=1)

# 添加标题、标签和图例
plt.title('Voltage vs. Cumulative Capacity')
plt.xlabel('Cumulative Capacity (AH)')
plt.ylabel('Total Voltage (V)')
plt.grid(True)

# 保存图表为文件，而不是显示它
plt.savefig('Voltage_vs_Cumulative_Capacity3_2.png', dpi=300, bbox_inches='tight')
