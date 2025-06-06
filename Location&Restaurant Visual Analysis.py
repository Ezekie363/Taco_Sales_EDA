import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('taco_sales_(2024-2025)_副本.csv')


# # 各城市taco餐厅数量排序
# city_order_counts = df['Location'].value_counts().sort_values(ascending=False)
# plt.figure(figsize=(10, 6))
# bars = plt.bar(city_order_counts.index, city_order_counts.values, color='skyblue')
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 2, str(height), ha='center', fontsize=9)
# plt.title('Location Order', fontsize=14)
# plt.xlabel('Location', fontsize=12)
# plt.ylabel('Order Count', fontsize=12)
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# plt.show()
#
#
#
# Chicago_Restaurant_Order = df[df['Location'] == 'Chicago']['Restaurant Name'].value_counts().sort_values(ascending=True)
#
# plt.figure(figsize=(10, 8))  # 竖直空间更大
#
# bars = plt.barh(Chicago_Restaurant_Order.index, Chicago_Restaurant_Order.values, color='green')
#
#
# for bar in bars:
#     width = bar.get_width()
#     plt.text(width + 0.3, bar.get_y() + bar.get_height() / 2, str(int(width)), va='center', fontsize=9)
#
# plt.title('Chicago Restaurant Orders', fontsize=14)
# plt.xlabel('Number of Orders', fontsize=12)
# plt.ylabel('Restaurant Name', fontsize=12)
#
# plt.tight_layout()
#
# plt.show()
#
#
# mostpopular_restaurant_order = df['Restaurant Name'].value_counts().sort_values(ascending=False)
# df['total'] = (df['Price ($)'] + df['Tip ($)'])
# mostpopular_restaurant_sales = df.groupby(['Restaurant Name'])['total'].sum().sort_values(ascending=False)
#
#
# # ---------- 图一：订单数量 ----------
# plt.figure(figsize=(10, 6))
# bars1 = plt.barh(mostpopular_restaurant_order.index, mostpopular_restaurant_order.values, color='skyblue')
# plt.title('Top 10 Restaurants by Order Count', fontsize=14)
# plt.xlabel('Number of Orders', fontsize=12)
# plt.ylabel('Restaurant Name', fontsize=12)
#
# for bar in bars1:
#     width = bar.get_width()
#     plt.text(width + 1.5, bar.get_y() + bar.get_height() / 2,
#              str(int(width)), va='center', fontsize=9)
#
# plt.gca().invert_yaxis()
# plt.tight_layout()
# plt.show()
#
#
# # ---------- 图二：销售额 ----------
# plt.figure(figsize=(10, 6))
# bars2 = plt.barh(mostpopular_restaurant_sales.index, mostpopular_restaurant_sales.values, color='lightgreen')
# plt.title('Top 10 Restaurants by Total Sales ($)', fontsize=14)
# plt.xlabel('Total Sales ($)', fontsize=12)
# plt.ylabel('Restaurant Name', fontsize=12)
#
# for bar in bars2:
#     width = bar.get_width()
#     plt.text(width + 1.5, bar.get_y() + bar.get_height() / 2,
#              f"{width:.2f}$", va='center', fontsize=9)
#
# plt.gca().invert_yaxis()
# plt.tight_layout()
# plt.show()



df['Order Time'] = pd.to_datetime(df['Order Time'], format='%d-%m-%Y %H:%M')

# 计算每行订单的总金额
df['total'] = df['Price ($)'] + df['Tip ($)']

# 提取月份（格式如 '2024-08'）
df['Month'] = df['Order Time'].dt.to_period('M')

# # 按月汇总销售额
# monthly_sales = df.groupby('Month')['total'].sum().sort_index()
#
# # 折线图可视化
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', color='teal', linestyle='-')
#
# # 添加数据标签
# for i, value in enumerate(monthly_sales.values):
#     plt.text(i, value + 1, f"${value:,.2f}", ha='center', fontsize=9)
#
# plt.title('Monthly Taco Sales Amount', fontsize=14)
# plt.xlabel('Month', fontsize=12)
# plt.ylabel('Sales Amount ($)', fontsize=12)
# plt.xticks(rotation=45)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()
#
#
# # 按月统计订单数量
# monthly_orders = df.groupby('Month').size().sort_index()
#
# # 折线图
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_orders.index.astype(str), monthly_orders.values, marker='o', color='orange', linestyle='-')
#
# # 添加数据标签
# for i, value in enumerate(monthly_orders.values):
#     plt.text(i, value + 1, str(value), ha='center', fontsize=9)
#
# plt.title('Monthly Taco Order Count', fontsize=14)
# plt.xlabel('Month', fontsize=12)
# plt.ylabel('Number of Orders', fontsize=12)
# plt.xticks(rotation=45)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()



# # 分组统计
# summary = df.groupby('Weekend Order').agg(
#     Order_Count=('total', 'count'),
#     Avg_Spending=('total', 'mean')
# ).rename(index={True: 'Weekend', False: 'Weekday'})
#
# # 横坐标
# x = np.arange(len(summary.index))  # ['Weekday', 'Weekend']
# width = 0.4
#
# fig, ax1 = plt.subplots(figsize=(10, 6))
#
# # 左侧 Y 轴：订单数量柱状图
# bars1 = ax1.bar(x - width/2, summary['Order_Count'], width, label='Order Count', color='#1f77b4')
# ax1.set_ylabel('Order Count', color='#1f77b4')
# ax1.tick_params(axis='y', labelcolor='#1f77b4')
#
# # 添加订单数量标签
# for i in range(len(x)):
#     ax1.text(x[i] - width/2, summary['Order_Count'].iloc[i] + 10, int(summary['Order_Count'].iloc[i]),
#              ha='center', fontsize=9, color='#1f77b4')
#
# # 设置 x 轴标签
# ax1.set_xticks(x)
# ax1.set_xticklabels(summary.index)
#
# # 右侧 Y 轴：平均花费柱状图
# ax2 = ax1.twinx()
# bars2 = ax2.bar(x + width/2, summary['Avg_Spending'], width, label='Avg Spending ($)', color='#ff7f0e')
# ax2.set_ylabel('Average Spending ($)', color='#ff7f0e')
# ax2.tick_params(axis='y', labelcolor='#ff7f0e')
#
# # 添加平均花费标签
# for i in range(len(x)):
#     ax2.text(x[i] + width/2, summary['Avg_Spending'].iloc[i] + 0.1, f"{summary['Avg_Spending'].iloc[i]:.2f}",
#              ha='center', fontsize=9, color='#ff7f0e')
#
# # 标题 & 布局
# plt.title('Order Count and Average Spending: Weekday vs Weekend', fontsize=14)
# fig.tight_layout()
# plt.show()



# # 按 Taco Size 分组，计算平均售价和订单数量
# summary = df.groupby('Taco Size').agg({
#     'Price ($)': 'mean',
#     'Taco Size': 'count'  # 用于计数
# }).rename(columns={
#     'Price ($)': 'Avg_Price',
#     'Taco Size': 'Order_Count'
# })
#
#
# # 准备数据
# x = np.arange(len(summary))
# width = 0.4
#
# fig, ax1 = plt.subplots(figsize=(10, 6))
#
# # 左轴：订单数柱状图
# bars1 = ax1.bar(x - width/2, summary['Order_Count'], width, label='Order Count', color='#1f77b4')
# ax1.set_ylabel('Order Count', color='#1f77b4')
# ax1.tick_params(axis='y', labelcolor='#1f77b4')
#
# # 添加订单数标签
# for i, v in enumerate(summary['Order_Count']):
#     ax1.text(x[i] - width/2, v + 7, int(v), ha='center', fontsize=9)
#
# # 右轴：平均售价柱状图
# ax2 = ax1.twinx()
# bars2 = ax2.bar(x + width/2, summary['Avg_Price'], width, label='Avg Price ($)', color='#ff7f0e')
# ax2.set_ylabel('Avg Price ($)', color='#ff7f0e')
# ax2.tick_params(axis='y', labelcolor='#ff7f0e')
#
# # 添加平均价格标签
# for i, v in enumerate(summary['Avg_Price']):
#     ax2.text(x[i] + width/2, v + 0.1, f"{v:.2f}", ha='center', fontsize=9)
#
# # 设置x轴
# plt.xticks(x, summary.index)
# plt.title('Taco Size vs Avg Price and Order Count')
# fig.tight_layout()
# plt.show()


#
# # 设置样式
# sns.set(style="whitegrid")
# plt.figure(figsize=(8, 6))
#
# # 箱线图
# sns.boxplot(
#     x='Toppings Count',
#     y='Price ($)',
#     data=df,
#     showmeans=True,
#     meanprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "black"},
# )
#
# # 添加标题和坐标轴标签
# plt.title('Boxplot: Price by Toppings Count')
# plt.xlabel('Toppings Count')
# plt.ylabel('Price ($)')
#
# # 添加均值标注
# grouped = df.groupby('Toppings Count')['Price ($)'].mean()
# for i, (topping, avg_price) in enumerate(grouped.items()):
#     plt.text(i, avg_price + 0.5, f'{avg_price:.2f}', ha='center', fontsize=9, color='black')
#
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(8, 6))
#
# # 回归图
# sns.regplot(
#     x='Toppings Count',
#     y='Price ($)',
#     data=df,
#     scatter_kws={'alpha': 0.3},
#     line_kws={'color': 'red'}
# )
#
# # 添加标题和坐标轴标签
# plt.title('Regression: Price vs Toppings Count')
# plt.xlabel('Toppings Count')
# plt.ylabel('Price ($)')
#
# plt.tight_layout()
# plt.show()




