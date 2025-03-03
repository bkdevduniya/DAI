import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# Display the first few rows of the dataframe to understand the structure
print(df.head())

# Convert 'price' and 'age' columns to numeric if they aren't already
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# 1. Grouping by 'Age_Group', 'Customer_Type', and 'Price_Range' and computing summary statistics
grouped = df.groupby(['Age_Group', 'Customer_Type', 'Price_Range']).agg(
    price_mean=('price', 'mean'),
    price_median=('price', 'median'),
    age_mean=('age', 'mean'),
    age_median=('age', 'median'),
    customer_count=('item_id', 'count')
).reset_index()

print(grouped)

# 2. Correlation analysis between 'price' and 'age'
correlation = df[['price', 'age']].corr()
print("\nCorrelation between Price and Age:")
print(correlation)

# Visualizing the correlation matrix
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap between Price and Age")
plt.show()

# 3. Visualizing the distribution of price based on Customer_Type and Price_Range
plt.figure(figsize=(12, 6))
sns.boxplot(x='Customer_Type', y='price', hue='Price_Range', data=df)
plt.title("Price Distribution by Customer Type and Price Range")
plt.show()

# 4. Violin plot to show age distribution across different customer types and price ranges
plt.figure(figsize=(12, 6))
sns.violinplot(x='Customer_Type', y='age', hue='Price_Range', split=True, data=df)
plt.title("Age Distribution by Customer Type and Price Range")
plt.show()

# 5. Visualizing the count of customers based on Age_Group and Customer_Status
plt.figure(figsize=(12, 6))
sns.countplot(x='Age_Group', hue='Customer_Status', data=df)
plt.title("Customer Count by Age Group and Status")
plt.show()
