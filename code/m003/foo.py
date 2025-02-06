# author: @alonzi
# date: 2025-02-05
# description: This is a test script to demonstrate the use of ai to generate code.

# import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# generate a random dataset of standard normal variables with n=1000000
data = np.random.randn(1000000)

'''
# plot the histogram of the data
plt.figure(figsize=(10, 6))  # Make the plot a bit larger
plt.hist(data, bins=100)

# Customize the plot
plt.tick_params(direction='in')  # Move ticks to inside
plt.grid(True, linestyle='--', alpha=0.7)  # Add gridlines

# Make axis labels larger and bold
plt.xlabel('Value', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')

# Make tick labels COMICALLY large
plt.xticks(fontsize=24)  # Doubled from an already large size
plt.yticks(fontsize=24)  # Doubled from an already large size

plt.show()
'''

# store data pandas dataframe
df = pd.DataFrame(data)

'''
# plot the histogram of the data
df.hist(bins=100)

# show the plot
plt.show()
'''

# print the first 5 rows of the dataframe
print(df.head())

# print the last 5 rows of the dataframe
print(df.tail())

