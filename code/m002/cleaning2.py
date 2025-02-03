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
cols = df.columns
print(cols)

for col in cols:
    if(col=="Actual gross"): print(col)
    print(df[col].head())

print(cols[3])

#print("<><><><><><>")
#print(df['Actual gross'].head())
