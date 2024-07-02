import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data of lead acid battery.xls')

# 计算每个循环的充电容量和放电容量的平均值
charge_avg_capacities = {}
discharge_avg_capacities = {}

# 对每个循环进行处理
for cycle, group in df.groupby('循环'):
    charge_capacities = group[group['充/放'] == 'CH']['充电容量(AH)']
    discharge_capacities = group[group['充/放'] == 'DIS']['放电容量(AH)']

    if not charge_capacities.empty:
        charge_avg_capacities[cycle] = charge_capacities.mean()
    if not discharge_capacities.empty:
        discharge_avg_capacities[cycle] = discharge_capacities.mean()

    # 将字典转换为有序的数据框，以便绘图
charge_avg_df = pd.DataFrame.from_dict(charge_avg_capacities, orient='index', columns=['Charge Capacity (AH)'])
discharge_avg_df = pd.DataFrame.from_dict(discharge_avg_capacities, orient='index', columns=['Discharge Capacity (AH)'])

# 对数据框进行排序，确保循环次数是按顺序的
charge_avg_df.sort_index(inplace=True)
discharge_avg_df.sort_index(inplace=True)

# 绘制容量随循环次数变化的曲线
plt.figure(figsize=(10, 6))
plt.plot(charge_avg_df.index, charge_avg_df['Charge Capacity (AH)'], label='Average Charge Capacity', marker='o')
plt.plot(discharge_avg_df.index, discharge_avg_df['Discharge Capacity (AH)'], label='Average Discharge Capacity',
         marker='x')
plt.title('Capacity Degradation Curve Over Cycles')
plt.xlabel('Cycle Number')
plt.ylabel('Average Capacity (AH)')
plt.legend()
plt.grid(True)
plt.savefig('capacity_degradation_curve2_1.png', bbox_inches='tight')
plt.close()