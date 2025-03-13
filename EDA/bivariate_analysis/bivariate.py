import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# perfoeming the bivariate analysis on price and coustumer age columns

df=pd.read_csv('cleaned_data.csv')

#printing the correlation matrix between price and age
matrix=df[['price','age']].corr()
print("printing the correlation matrix \n",matrix)


# scatter plot between price and age
df.plot.scatter(y='price',x='age',s=10)
plt.show()


# relationship between price and Age_group,costumer_type
data1=df.groupby(['Age_Group'])['price'].sum()
data2=df.groupby(['Customer_Type'])['price'].sum()
data3=df.groupby(['Price_Range'])['price'].sum()



# bar plots of price vs Age_group,Customer_Type,Customer_Status
ax=sns.barplot(x=data1.index,y=data1.values)
ax.set(xlabel='Age_Group',ylabel='price',title='bar plot oprice vs Age_group')
plt.show()

ax=sns.barplot(x=data2.index,y=data2.values)
ax.set(xlabel='Customer_Type',ylabel='price',title='bar plot of price vs Customer_Type')
plt.show()

ax=sns.barplot(x=data3.index,y=data3.values)
ax.set(xlabel='Price_Range',ylabel='price',title='bar plot of price vs Price_Range')
plt.show()

# box plots of price vs Age_group,Customer_Type,Customer_Status
ax=sns.boxplot(data=df,x='Age_Group',y='price')
ax.set(xlabel='Age_Group',ylabel='price',title='box plot oprice vs Age_group')
plt.show()

ax=sns.boxplot(data=df,x='Customer_Type',y='price')
ax.set(xlabel='Customer_Type',ylabel='price',title='bar plot of price vs Customer_Type')
plt.show()

ax=sns.boxplot(data=df,x='Price_Range',y='price')
ax.set(xlabel='Price_Range',ylabel='price',title='bar plot of price vs Price_Range')
plt.show()

# violin plots of price vs Age_group,Customer_Type,Customer_Status
ax=sns.violinplot(x='Age_Group',y='price',data=df)
ax.set(xlabel='Age_Group',ylabel='price',title='violin plot of price vs Age_group')
plt.show()

ax=sns.violinplot(x='Customer_Type',y='price',data=df)
ax.set(xlabel='Customer_Type',ylabel='price',title='violin plot of price vs Customer_Type')
plt.show()

ax=sns.violinplot(x='Customer_Status',y='price',data=df)
ax.set(xlabel='Customer_Status',ylabel='price',title='violin plot of price vs Customer_Status')
plt.show()
