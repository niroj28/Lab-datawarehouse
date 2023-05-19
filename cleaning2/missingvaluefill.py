import pandas as pd

data = pd.read_csv('employee.csv')
print("Original Data")
print(data[0:25])

# Filling missing values with mean 

data['Salary']=data['Salary'].fillna(data['Salary'].mean())
print("\nCleaned Data by Mean")
print(data[0:25])

data = pd.read_csv('employee.csv')
print("\nOriginal Data")
print(data[0:25])

# Filling missing values within
data['Salary']=data['Salary'].interpolate(method="linear")
print("\nCleaned Data by Linear interpolation")
print(data[0:25])