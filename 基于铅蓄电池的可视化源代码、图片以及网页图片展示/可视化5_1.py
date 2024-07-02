import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 读取数据
df = pd.read_excel('data of lead acid battery.xls')

# 数据清洗和准备
numeric_cols = ['电流(A)', '总电压(V)', '电池1(V)', '电池2(V)', '电池3(V)', '电池4(V)', '电池5(V)', '电池6(V)',
                '充电容量(AH)', '放电容量(AH)', '环境温度(°C)']
df_numeric = df[numeric_cols].dropna()  # 移除包含NaN值的行

# 设置中文字体（如果需要）
plt.rcParams['font.sans-serif'] = 'SimHei'  # 确保你的系统中有这个字体

# 绘制散点矩阵图
plt.figure(figsize=(12, 10))
# 使用seaborn的PairGrid来避免'mode.use_inf_as_null'的问题
g = sns.PairGrid(df_numeric)
g.map_diag(sns.kdeplot)  # 使用kdeplot替换histplot以避免配置选项错误
g.map_offdiag(sns.scatterplot)
g.fig.suptitle('电池参数散点矩阵图', fontsize=16)  # 使用中文标题
plt.savefig('scatter_matrix_plot5_1.png')  # 保存为PNG图片
plt.close()

# 绘制热力图
plt.figure(figsize=(10, 8))
corr_matrix = df_numeric.corr()  # 计算相关性矩阵
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')  # 绘制热力图
plt.title('电池参数相关性热力图')  # 使用中文标题
plt.savefig('correlation_heatmap5_2.png')  # 保存为PNG图片
plt.close()