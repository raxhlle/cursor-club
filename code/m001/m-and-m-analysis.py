#author: @ryan-healy
#date: 2025-01-22
#description: M&M analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Change working directory to m001
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#load data
df = pd.read_csv('m-and-m-data.csv')

print(df.head())

#count how many m&m's are in all the bags
print(df['Blue'].value_counts())

#add up all the numbers in the Blue column
print(df['Blue'].sum())

#new dataframe that's the first 5 lines of the old one
df_5 = df.head(5)
print(df_5)

#type cast the Brown column from a string into an integer
df_5['Brown'] = df_5['Brown'].astype(int)

#do the same for the other colors
print(df_5['Brown'].sum())
print(df_5['Green'].sum())
print(df_5['Orange'].sum())
print(df_5['Red '].sum())
print(df_5['Yellow'].sum())

#do the sum of all the columns
print(df_5.sum())

'''
df['Brown'] = df['Brown'].astype(int)
print(df['Brown'].sum())
'''

# Remove rows with NaN values and problematic data
df_clean = df[df['Brown'] != '1,,jj'].dropna()
print("\nShape before cleaning:", df.shape)
print("Shape after removing NaN and bad data:", df_clean.shape)

# Alternatively, to remove NaN values from specific columns only:
df_clean_columns = df[df['Brown'] != '1,,jj'].dropna(subset=['Brown', 'Blue', 'Green', 'Orange', 'Red ', 'Yellow'])
print("\nShape after removing NaN from color columns:", df_clean_columns.shape)

df_clean_columns['Brown'] = df_clean_columns['Brown'].astype(int)
print(df_clean_columns['Brown'].sum())

print(df_clean_columns.sum())