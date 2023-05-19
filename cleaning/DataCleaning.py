# Lab 2.1 : Data Cleaning
import pandas as pd
import numpy as np

data = pd.read_csv('employee.csv')
print("Original Data")
print(data[0:25])

# Removing missing values
data = data.dropna(axis=0)

# Removing duplicate rows
data.drop_duplicates(keep='first', inplace=True)

# Removing column Bonus %
del data['Bonus %']

# Correcting Inconsistencies among values
data['Team'] = data['Team'].str.replace('Fin', 'Finance')
data['Team'] = data['Team'].str.replace('Mkt', 'Marketing')
data['Team'] = data['Team'].str.replace('Sal', 'Sales')
data['Team'] = data['Team'].str.replace('IT', 'Information Technology')

print("\nCleaned Data")
print(data[0:25])
data.to_csv('Employee_cleaned.csv', index=False)
print("Successfully Cleaned...")
