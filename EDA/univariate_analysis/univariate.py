import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# perfoeming the univariate analysis on price and coustumer age columns

df=pd.read_csv('cleaned_data.csv')
print("statistical summary of price column")
print(df['price'].describe(),"\n")
print("price skewness  ",df['price'].skew())
print("price standard deviation    ",df['price'].std())
print("price variance   ",df['price'].var(),"\n\n")

print("statistical summary of age column")
print(df['age'].describe(),"\n")
print("age skewness  ",df['age'].skew())
print("age standard deviation    ",df['age'].std())
print("age variance   ",df['age'].var(),"\n\n")


# grouping the data based on Age_Group column
print("frequency distribution on Age_Group column")
data3=df.groupby(['Age_Group']).size()
print(data3,"\n\n")

# grouping the data based on Customer_Status column
print("frequency distribution on Customer_Status column")
data4=df.groupby(['Customer_Status']).size()
print(data4,"\n\n")


# grouping the data based on Price_Range column
print("frequency distribution on Price_Range column")
data5=df.groupby(['Price_Range']).size()
print(data5,"\n\n")

# grouping the data based on Customer_Status column
print("frequency distribution on Customer_Status column")
data6=df.groupby(['Customer_Type']).size()
print(data6,"\n\n")

ax=sns.barplot(x=data3.index,y=data3.values)
ax.set(xlabel='Age_Group',ylabel='count',title='frequency distribution of Age_group')
plt.show()

ax=sns.boxplot(data3)
ax.set(xlabel='Age_Group',ylabel='count',title='frerquency distribution of Age_group')
plt.show()

ax=sns.barplot(x=data4.index,y=data4.values)
ax.set(xlabel='Customer_Status',ylabel='count',title='frequency distribution of Customer_Status')
plt.show()

ax=sns.boxplot(data4)
ax.set(xlabel='Customer_Status',ylabel='count',title='freq. dist. of Customer_Status')
plt.show()

ax=sns.barplot(x=data6.index,y=data6.values)
ax.set(xlabel='Customer_Type',ylabel='count',title='frequency distribution of Customer_Type')
plt.show()

ax=sns.boxplot(data6)
ax.set(xlabel='Customer_Type',ylabel='count',title='freq. dist. of Customer_Type')
plt.show()


ax=sns.barplot(x=data5.index,y=data5.values)
ax.set(xlabel='Price_Range',ylabel='count',title='freq. dist. of Price_Range')
plt.show()

ax=sns.boxplot(data5)
ax.set(xlabel='Price_Range',ylabel='count',title='freq. dist. of Price_Range')
plt.show()
