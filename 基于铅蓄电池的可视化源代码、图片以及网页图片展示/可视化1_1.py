import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
df = pd.read_excel("data of lead acid battery.xls")


# 定义函数处理capacity，区分充电和放电阶段
def process_capacity(group):
    group['charge_cap'] = group['充电容量(AH)'].cumsum()
    group['discharge_cap'] = group['放电容量(AH)'].cumsum()
    return group


# 依据循环进行分组，处理每个循环的数据
df = df.groupby('循环', as_index=False).apply(process_capacity)
df['total_cap'] = np.where(df['充/放'] == 'CH', df['charge_cap'], df['discharge_cap'])
# 设置图表的颜色和样式
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
linestyles = ['-', '--']
markers = ['o', 's', '^', 'D', '*', 'p']
plt.style.use('seaborn-whitegrid')
# 绘制电压、电流、温度与容量的关系图
fig, axs = plt.subplots(3, 1, figsize=(10, 15), dpi=100, sharex=True, gridspec_kw={'hspace': 0})


# 定义绘制图表的函数
def plot_parameter_vs_capacity(df, parameter, title, ylabel, color_charge, color_discharge, filename):
    plt.figure(figsize=(10, 5))  # 创建一个新图表
    for cycle, group in df.groupby('循环'):
        charge_data = group[group['充/放'] == 'CH']
        discharge_data = group[group['充/放'] == 'DIS']
        plt.plot(charge_data['total_cap'], charge_data[parameter], color=color_charge, linestyle='-',
                 label=f'Cycle {cycle} Charge' if cycle == min(df['循环']) else None)
        plt.plot(discharge_data['total_cap'], discharge_data[parameter], color=color_discharge, linestyle='--',
                 label=f'Cycle {cycle} Discharge' if cycle == min(df['循环']) else None)
    plt.title(title)
    plt.xlabel('Capacity (Ah)')
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # 关闭当前图表，以便绘制下一个图表


# 分别绘制电压、电流、温度与容量的关系图，并保存为不同的文件
plot_parameter_vs_capacity(df, '总电压(V)', 'Voltage vs. Capacity', 'Voltage (V)', '#1f77b4', '#ff7f0e',
                           'voltage_vs_capacity1_1.png')
plot_parameter_vs_capacity(df, '电流(A)', 'Current vs. Capacity', 'Current (A)', '#2ca02c', '#d62728',
                           'current_vs_capacity1_2.png')
plot_parameter_vs_capacity(df, '环境温度(°C)', 'Ambient Temperature vs. Capacity', 'Temperature (°C)', '#9467bd',
                           '#8c564b', 'temperature_vs_capacity1_3.png')
