import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data of lead acid battery.xls')

# 筛选特定循环次数的数据
cycles_to_plot = [10, 20, 30, 40, 50, 60, 70, 80]
df_filtered = df[df['循环'].isin(cycles_to_plot)]


# 定义绘图函数
def plot_parameter_vs_capacity(df, parameter, title, save_path):
    plt.figure(figsize=(12, 6))
    for cycle in cycles_to_plot:
        cycle_data = df[df['循环'] == cycle]
        charge_mask = cycle_data['充/放'] == 'CH'
        discharge_mask = ~charge_mask

        # 绘制充电曲线
        plt.plot(cycle_data.loc[charge_mask, '充电容量(AH)'], cycle_data.loc[charge_mask, parameter],
                 label=f'Cycle {cycle} Charge')
        # 绘制放电曲线
        plt.plot(cycle_data.loc[discharge_mask, '放电容量(AH)'], cycle_data.loc[discharge_mask, parameter],
                 linestyle='--', label=f'Cycle {cycle} Discharge')

    plt.title(title)
    plt.xlabel('Capacity (Ah)')
    plt.ylabel(parameter)
    plt.legend(fontsize=6)  # 设置图例字体大小
    plt.grid(True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # 保存为PNG图片
    plt.close()  # 关闭当前图表，释放资源


# 绘制并保存图表
plot_parameter_vs_capacity(df_filtered, '总电压(V)', 'Voltage vs Capacity', 'Voltage_vs_Capacity1_4.png')
plot_parameter_vs_capacity(df_filtered, '电流(A)', 'Current vs Capacity', 'Current_vs_Capacity1_5.png')
plot_parameter_vs_capacity(df_filtered, '环境温度(°C)', 'Temperature vs Capacity', 'Temperature_vs_Capacity1_6.png')
