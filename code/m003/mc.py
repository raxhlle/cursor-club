# Monte Carlo simulation example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define list of fruits and their probabilities
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
probabilities = [0.3, 0.25, 0.2, 0.15, 0.1]  # Must sum to 1

# Number of simulations
n_simulations = 1000

# Run Monte Carlo simulation
results = np.random.choice(fruits, size=n_simulations, p=probabilities)

# Convert results to DataFrame
df_results = pd.DataFrame(results, columns=['fruit'])

# Calculate frequencies
frequencies = df_results['fruit'].value_counts()
relative_frequencies = df_results['fruit'].value_counts(normalize=True)

print("\nActual frequencies:")
print(frequencies)
print("\nRelative frequencies (should be close to original probabilities):")
print(relative_frequencies)

'''
# Optional visualization
plt.figure(figsize=(10, 6))
plt.bar(frequencies.index, frequencies.values)
plt.title('Monte Carlo Simulation Results')
plt.xlabel('Fruit')
plt.ylabel('Frequency')
plt.show()
''' 