import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data of lead acid battery.xls')


# 辅助函数，用于计算并绘制dQ/dV曲线
def calculate_and_plot_dq_dv(df, charge_or_discharge, filename=None):
    # 筛选充电或放电数据
    df_filtered = df[df['充/放'] == charge_or_discharge]

    # 计算dQ和dV
    df_filtered['dQ'] = df_filtered['充电容量(AH)'].diff() if charge_or_discharge == 'CH' else df_filtered[
        '放电容量(AH)'].diff()
    df_filtered['dV'] = df_filtered['总电压(V)'].diff()

    # 去除NaN值
    df_filtered = df_filtered.dropna(subset=['dQ', 'dV'])

    # 计算dQ/dV
    df_filtered['dQ/dV'] = df_filtered['dQ'] / df_filtered['dV']

    # 绘制dQ/dV曲线
    fig, axs = plt.subplots(nrows=4, figsize=(12, 16))

    # 电压为横坐标
    axs[0].plot(df_filtered['总电压(V)'], df_filtered['dQ/dV'], marker='o', linestyle='-',
                color='blue' if charge_or_discharge == 'CH' else 'red')
    axs[0].set_title(f'dQ/dV Curve with Voltage as X-axis ({charge_or_discharge})')
    axs[0].set_xlabel('Voltage (V)')
    axs[0].set_ylabel('dQ/dV (AH/V)')

    # 电流为横坐标
    axs[1].plot(df_filtered['电流(A)'], df_filtered['dQ/dV'], marker='o', linestyle='-',
                color='blue' if charge_or_discharge == 'CH' else 'red')
    axs[1].set_title(f'dQ/dV Curve with Current as X-axis ({charge_or_discharge})')
    axs[1].set_xlabel('Current (A)')
    axs[1].set_ylabel('dQ/dV (AH/V)')

    # 容量为横坐标
    capacity_column = '充电容量(AH)' if charge_or_discharge == 'CH' else '放电容量(AH)'
    axs[2].plot(df_filtered[capacity_column], df_filtered['dQ/dV'], marker='o', linestyle='-',
                color='blue' if charge_or_discharge == 'CH' else 'red')
    axs[2].set_title(f'dQ/dV Curve with Capacity as X-axis ({charge_or_discharge})')
    axs[2].set_xlabel('Capacity (AH)')
    axs[2].set_ylabel('dQ/dV (AH/V)')

    # 环境温度为横坐标
    axs[3].plot(df_filtered['环境温度(°C)'], df_filtered['dQ/dV'], marker='o', linestyle='-',
                color='blue' if charge_or_discharge == 'CH' else 'red')
    axs[3].set_title(f'dQ/dV Curve with Ambient Temperature as X-axis ({charge_or_discharge})')
    axs[3].set_xlabel('Ambient Temperature (°C)')
    axs[3].set_ylabel('dQ/dV (AH/V)')

    if filename:
        plt.savefig(filename, bbox_inches='tight')


# 绘制充电和放电的dQ/dV曲线，并保存为图片
calculate_and_plot_dq_dv(df, 'CH', 'charge_dq_dv_curve4_1.png')  # 充电，并保存为"charge_dq_dv_curve.png"
calculate_and_plot_dq_dv(df, 'DIS', 'discharge_dq_dv_curve4_2.png')  # 放电，并保存为"discharge_dq_dv_curve.png"
