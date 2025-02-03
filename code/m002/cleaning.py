# author: Abel Addis
# date: 2025-01-29
# description: cleaning data

import pandas as pd
import matplotlib.pyplot as plt

# load data
filepath = 'code/m002/data.csv'

df = pd.read_csv(filepath)

print(df.head())

#show the columns
print(df.columns)

#summarize the data
print(df.describe())

# Basic cleaning steps
# 1. Remove any duplicate rows
df = df.drop_duplicates()

# 2. Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 3. Reset index after cleaning
#df = df.reset_index(drop=True)

print("\nShape of cleaned dataset:", df.shape)

#summarize the cleaned data
print("\nSummary of cleaned data:")





print(df.describe())

print(df.head())

#actual gross
#print(df['Actual gross'].head())

print("\nExact column names:")
for col in df.columns:
    print(f"'{col}'")  # This will show exact names with any spaces or special characters

