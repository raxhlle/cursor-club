import matplotlib.pyplot as plt
import numpy as np

# Data from the image
codes_remaining = [1296, 216, 36, 6, 1]
entropy = [10.34, 7.75, 5.2, 2.58, 0]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(codes_remaining, entropy, marker='o', linewidth=2, markersize=8)

# Add labels and title
plt.xlabel('Possible Codes Remaining (N)', fontsize=12)
plt.ylabel('Entropy (H) (log₂(N))', fontsize=12)
plt.title('Entropy vs Possible Codes Remaining', fontsize=14)

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Reverse x-axis since the values decrease
plt.xscale('log')  # Use log scale for better visualization
plt.gca().invert_xaxis()

# Add data point labels
for x, y in zip(codes_remaining, entropy):
    plt.annotate(f'({x}, {y})', 
                (x, y), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center')

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the plot
plt.savefig('entropy_plot.png')
plt.show() 