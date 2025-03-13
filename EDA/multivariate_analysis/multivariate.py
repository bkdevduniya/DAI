import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('cleaned_data.csv')

#drawing the pair plot  between price and age
sns.pairplot(df)
plt.show()

# drawing the heatmap between price and age
sns.heatmap(df[['price','age']].corr(),annot=True)
plt.show()
