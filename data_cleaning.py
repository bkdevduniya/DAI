import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('data.csv')

# printng the duplicate rows
print("printng the duplicate rows \n",df[df.duplicated()])

#removing duplicate rows
df.drop_duplicates(inplace=True)

# printing after removing duplicates
print("printing after removing duplicates \n",df)

# after removing duplicate rows checking presence of any duplicate rows further
print("after removing duplicate rows checking presence of any duplicate rows further \n",df.duplicated())

# statistical summary of data before replacing the null values
print("statistical summary of data before replacing the null values \n",df.describe())

# checking presence of any missing value in all columns
print("checking presence of any missing value in all columns \n",df.isnull().any())

# removing the rows with missing values
df.dropna(inplace=True)
# calculating the statictical summary of the dataset after replacing missing values
print("calculating the statictical summary of the dataset after removing the null values \n",df.describe())

# checking presence of any missing value in all columns
print("checking presence of any missing value in all columns after removing the rows with missing values\n",df.isnull().any())

print("statistical data before removing outliers \n",df.describe())


# graphically detecting the outliers using box-plot of column price

sns.boxplot(df['price'])
plt.show()

# now we will calculate the IQR of given dataset for the column price

# finding out the 25,50 and 75th percentile
Q1=df['price'].quantile(0.25)
Q2=df['price'].quantile(0.5)
Q3=df['price'].quantile(0.75)

IQR=Q3-Q1
print("\niqr_range_min :",Q1-1.5*IQR,"\niqr_range_max :",Q3+1.5*IQR)
# now the data points < Q1-1.5*IQR or > Q3+1.5*IQR are outliers

for i in df.index:
    if df.loc[i,'price'] < Q1-1.5*IQR or df.loc[i,'price']> Q3+1.5*IQR:
        print("outlier :",df.loc[i,'price'])
        df.drop(i,inplace=True)

print("\nstatistical data after removing outliers \n",df.describe())

# plotting the box plot after removing the outliers

Q1=df['price'].quantile(0.25)
Q2=df['price'].quantile(0.5)
Q3=df['price'].quantile(0.75)

IQR=Q3-Q1
print("modified_iqr_min :",Q1-1.5*IQR,"\n","mofdified_iqr_max :",Q3+1.5*IQR)

sns.boxplot(df['price'])
plt.show()

# standarization
print(df)
# Apply logic for setting Price_Range based on price
for i in df.index:
    val=df.loc[i,'price']
    if int(val) <=100:
        df.loc[i,'Price_Range'] = 'low'
    elif int(val) <= 400.0:
        df.loc[i,'Price_Range'] = 'medium'
    else:
        df.loc[i,'Price_Range'] = 'high'


# Standardizing Customer_Type based on Price_Range
for i in df.index:
    val=df['Price_Range'][i]
    if val=='low':
        df.loc[i,'Customer_Type'] = 'low spender'
    elif val=='medium':
        df.loc[i,'Customer_Type'] = 'medium spender'
    else:
        df.loc[i,'Customer_Type'] = 'high spender'

# Show the modified dataframe
print("Data frame after standardization:\n", df)

