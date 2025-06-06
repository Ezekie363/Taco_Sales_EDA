import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('taco_sales_(2024-2025)_副本.csv')
# print(df.columns) //查看数据字段


# # 1.按城市分组查看taco店的数量并排序
# taco_restaurant_num = df.groupby(['Location'])['Restaurant Name'].count().sort_values(ascending=False)
# print("Q1",taco_restaurant_num)
#
# # 2.各个城市taco店的平均送达时间
# taco_delivery_time = df.groupby(['Location'])['Delivery Duration (min)'].mean().round().sort_values(ascending=True)
# print("Q2",taco_delivery_time)
#
# # 3.taco类型有多少种
# taco_type = df['Taco Type'].unique()
# print("Q3",taco_type)
#
# # 4.加小料的taco与加小料的占比为多少
#
# # 计算不加小料的订单总和
# no_toppings = (df['Toppings Count'] == 0).sum()
# # 计算加小料的订单总和
# taco_toppings = (df['Toppings Count'] > 0).sum()
#
# # 计算加小料的taco占总体的比率
# toppings_rate1 = round(taco_toppings / (taco_toppings + no_toppings), 2)
#
# # 计算不加小料的taco占总体的比率
# toppings_rate2 = round(no_toppings / (taco_toppings + no_toppings), 2)
# print("Q4.1",toppings_rate1)
# print("Q4.2",toppings_rate2)

# # 5.周末下单的数量与非周末下单的数量比为多少
# weekend_order = df['Weekend Order'].sum() #周末下单
# non_weekend_order = (~df['Weekend Order']).sum() #非周末下单
#
# weekend_order_rate1 = round(weekend_order / (weekend_order + non_weekend_order), 2)
# weekend_order_rate2 = round(non_weekend_order / (weekend_order + non_weekend_order), 2)
#
# print("Q5.1",weekend_order_rate1)
# print("Q5.2",weekend_order_rate2)
#
# # 6.下单各个taco size的数量排序
# taco_size_sort = df['Taco Size'].value_counts().sort_values()
# print("Q6",taco_size_sort)
#
#
# # 7.加小料的taco平均价格为多少
# taco_toppings_price = df[df['Toppings Count'] > 0]['Price ($)'].mean().round(2)
# taco_non_toppings_price = df[df['Toppings Count'] ==0]['Price ($)'].mean().round(2) #不加小料的taco平均价格
#
# print("Q7.1",taco_toppings_price)
# print("Q7.2",taco_non_toppings_price)
#
# # 9.小费平均价格为多少
# tip_mean = df['Tip ($)'].mean().round(2)
# print("Q9",tip_mean)
#
# # 小费占taco价格的百分之多少
# taco_mean_price = df['Price ($)'].mean().round(2)
# taco_tip_rate = (tip_mean / taco_mean_price).round(2)
# print("Q9.1",taco_tip_rate)


# 10.taco type销量排序
tacop_type_sort = df['Taco Type'].value_counts().sort_values()
print("Q10",tacop_type_sort)


# 11.chicago城市的taco店排序
chicago_restaurant_counts = df[df['Location'] == 'Chicago']['Restaurant Name'].value_counts()
print("Q11芝加哥 🌮餐厅数量排序：\n",chicago_restaurant_counts)

# 12.有多少家不同的餐厅
restaurant_count = df['Restaurant Name'].value_counts()
print("Q12",restaurant_count)


# 13.总营销额为多少
total_sales = df['Price ($)'].sum()
print("Q13",total_sales,"$")

# 14.平均每份taco的价钱
tacoPrice_mean = df['Price ($)'].mean().round(2)
print("Q14",tacoPrice_mean)


# 15.加小料的taco平均贵了多少钱
taco_toppings_meanPrice = df[df['Toppings Count']>0]['Price ($)'].mean().round(2)
taco_Non_toppings_meanPrice = df[df['Toppings Count']==0]['Price ($)'].mean().round(2)

print("加小料平均价格：",taco_toppings_meanPrice )
print("不加小料平均价格：",taco_Non_toppings_meanPrice )

taco_toppings_EXP = taco_toppings_meanPrice - taco_Non_toppings_meanPrice
print("加小料的taco价格平均要贵：",taco_toppings_EXP )

# 16.全美最受欢的餐厅(按订单数/销售额排序)
mostpopular_restaurant_order = df['Restaurant Name'].value_counts().sort_values(ascending=False)
df['total'] = (df['Price ($)'] + df['Tip ($)'])
mostpopular_restaurant_sales = df.groupby(['Restaurant Name'])['total'].sum().sort_values(ascending=False)

print("Q16.1",mostpopular_restaurant_order)
print("Q16.2",mostpopular_restaurant_sales)

