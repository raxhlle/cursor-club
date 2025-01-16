import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 1102
std = 184
uva_mean = 1425  # Add UVA mean
x = np.linspace(mean - 4*std, mean + 4*std, 1000)  # Create range of scores

# Calculate normal distribution
y = norm.pdf(x, mean, std)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b-', lw=2, label='SAT Score Distribution')

# Fill areas for different sigma regions
plt.fill_between(x, y, where=(x >= mean-std) & (x <= mean+std), 
                color='red', alpha=0.2, label='±1σ (68.27%)')
plt.fill_between(x, y, where=(x >= mean-2*std) & (x <= mean+2*std), 
                color='yellow', alpha=0.1, label='±2σ (95.45%)')
plt.fill_between(x, y, where=(x >= mean-3*std) & (x <= mean+3*std), 
                color='green', alpha=0.1, label='±3σ (99.73%)')

# Add vertical lines for mean and standard deviations
plt.axvline(x=mean, color='black', linestyle='--', alpha=0.5, label='Mean')
for i in [-3, -2, -1, 1, 2, 3]:
    plt.axvline(x=mean + i*std, color='gray', linestyle='--', alpha=0.5)

# Add score labels at bottom
for i in [-3, -2, -1, 0, 1, 2, 3]:
    score = mean + i*std
    plt.text(score, -0.0005, f'{int(score)}', 
            horizontalalignment='center', fontsize=10)

# Add annotations for scores above mean
for i in [1, 2, 3]:
    score = mean + i*std
    height = norm.pdf(score, mean, std)
    # Add arrow and text
    plt.annotate(f'+{i}σ: {int(score)}\nTop {norm.sf(i):.1%}', 
                xy=(score, height),
                xytext=(score + 50, height + 0.0005),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10,
                fontweight='bold')

# Add UVA average annotation
uva_height = norm.pdf(uva_mean, mean, std)
uva_sigma = (uva_mean - mean) / std
plt.annotate(f'UVA Average: {uva_mean}\n({uva_sigma:.1f}σ, Top {norm.sf(uva_sigma):.1%})', 
            xy=(uva_mean, uva_height),
            xytext=(uva_mean - 100, uva_height + 0.001),
            arrowprops=dict(facecolor='orange', shrink=0.05),
            fontsize=10,
            fontweight='bold',
            color='darkblue')
plt.axvline(x=uva_mean, color='orange', linestyle='--', alpha=0.5)

# Add text box with statistics
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = '\n'.join([
    'Statistics:',
    f'Mean: {mean}',
    f'Std Dev: {std}',
    f'±1σ: {mean-std:.0f}-{mean+std:.0f}',
    f'±2σ: {mean-2*std:.0f}-{mean+2*std:.0f}',
    f'±3σ: {mean-3*std:.0f}-{mean+3*std:.0f}'
])
plt.text(0.95, 0.95, textstr, transform=plt.gca().transAxes, 
         verticalalignment='top', bbox=props)

# Customize the plot
plt.title('SAT Score Distribution with UVA Average', fontsize=14)
plt.xlabel('SAT Score', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Show the plot
plt.show()

# Optionally save the plot
# plt.savefig('sat_distribution.pdf') 