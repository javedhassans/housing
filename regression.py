# %%
import os

print(os.listdir())
path = 'C:\/Users\/javed\/PycharmProjects\/handsonmachinelearning\/housing'
os.chdir(path)
print(os.getcwd())
#%%
# importing all dependecies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import time
import sklearn
#%%
pd.set_option("max_rows", 30)
pd.set_option("max_columns", 30)
# %%
housing = pd.read_csv('housing.csv')
housing.head()
# %%
housing.info()
#%%
numeric_data = ['housing_median_age','total_rooms', 'total_bedrooms','population',
                'households', 'median_income', 'median_house_value' ]
sns.pairplot(data=housing[numeric_data])
plt.figure(figsize=(10,10))
plt.show()
#%%
sns.scatterplot(x=housing.median_income, y=housing.median_house_value,
                data=housing, markers=True)
plt.show()