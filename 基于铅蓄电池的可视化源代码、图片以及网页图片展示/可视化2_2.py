import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data of lead acid battery.xls')

# 找到每个循环的充电结束时的充电容量和放电结束时的放电容量
charge_capacities = []
discharge_capacities = []
cycles = sorted(df['循环'].unique())  # Ensure cycles are sorted

for cycle in cycles:
    cycle_data = df[df['循环'] == cycle]

    # Check if there is charge data for this cycle
    charge_data = cycle_data[cycle_data['充/放'] == 'CH']
    if not charge_data.empty:
        charge_capacities.append(charge_data['充电容量(AH)'].iloc[-1])
    else:
        charge_capacities.append(None)  # Or handle the missing data as appropriate

    # Check if there is discharge data for this cycle
    discharge_data = cycle_data[cycle_data['充/放'] == 'DIS']
    if not discharge_data.empty:
        discharge_capacities.append(discharge_data['放电容量(AH)'].iloc[-1])
    else:
        discharge_capacities.append(None)  # Or handle the missing data as appropriate

# Remove None values from the capacity lists and corresponding cycles
valid_cycles_charge = [cycle for cycle, cap in zip(cycles, charge_capacities) if cap is not None]
valid_charge_capacities = [cap for cap in charge_capacities if cap is not None]

valid_cycles_discharge = [cycle for cycle, cap in zip(cycles, discharge_capacities) if cap is not None]
valid_discharge_capacities = [cap for cap in discharge_capacities if cap is not None]

# 绘制充电容量随循环次数变化的曲线
plt.figure(figsize=(10, 5))
plt.plot(valid_cycles_charge, valid_charge_capacities, marker='o', label='Charge Capacity')
plt.title('Charge Capacity Trend Over Cycles')
plt.xlabel('Cycle Number')
plt.ylabel('Charge Capacity (AH)')
plt.legend()
plt.savefig('charge_capacity_trend2_2.png', bbox_inches='tight')
plt.close()

# 绘制放电容量随循环次数变化的曲线
plt.figure(figsize=(10, 5))
plt.plot(valid_cycles_discharge, valid_discharge_capacities, marker='o', label='Discharge Capacity')
plt.title('Discharge Capacity Trend Over Cycles')
plt.xlabel('Cycle Number')
plt.ylabel('Discharge Capacity (AH)')
plt.legend()
plt.savefig('discharge_capacity_trend2_3.png', bbox_inches='tight')
plt.close()