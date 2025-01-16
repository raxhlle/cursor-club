import sys
import subprocess

# Check and install required packages
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} has been installed")
        
print("Checking and installing required packages...")
# Install required packages if not present
install_package('numpy')
install_package('matplotlib')
print("All required packages are installed!")

# Only import after installation is complete
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing packages: {e}")
    sys.exit(1)

# Generate data points for x-axis
x = np.linspace(-4, 4, 1000)

# Calculate the standard normal distribution
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Standard Normal Distribution')
plt.fill_between(x, y, alpha=0.3)

# Add vertical dashed line at 1 standard deviation
plt.axvline(x=1, color='gray', linestyle='--', alpha=0.5)

# Add arrow and label for 1 standard deviation
x_arrow = 1  # 1 standard deviation
y_arrow = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_arrow**2)
plt.annotate('?', 
            xy=(x_arrow, y_arrow),
            xytext=(x_arrow + 0.7, y_arrow - 0.05),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            weight='bold')

# Add labels and title
plt.title('Standard Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.legend()

# Show the plot
plt.show()

# Optional: Generate random samples from the distribution
samples = np.random.standard_normal(1000)

# Create histogram and residual plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), height_ratios=[2, 1, 1], gridspec_kw={'hspace': 0.4})

# Upper plot (histogram)
hist_values, bin_edges, _ = ax1.hist(samples, bins=30, density=True, alpha=0.7, color='blue', label='Data (blue)')
ax1.plot(x, y, 'r-', label='Theoretical Distribution')
ax1.set_title('Histogram of Random Samples vs Standard Normal Distribution')
ax1.set_xlabel('x')
ax1.set_ylabel('Probability Density')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Middle plot (residuals)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
theoretical_values = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * bin_centers**2)
residuals = hist_values - theoretical_values

ax2.plot(bin_centers, residuals, 'k.-', label='Residuals')
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.3)
ax2.set_title('Residuals (Data - Theoretical)')
ax2.set_xlabel('x')
ax2.set_ylabel('Difference')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Import scipy for statistical tests
try:
    from scipy import stats
except ImportError:
    install_package('scipy')
    from scipy import stats

# New bottom plot (histogram of residuals)
# Fit normal distribution to residuals
residual_mean = np.mean(residuals)
residual_std = np.std(residuals)
residual_x = np.linspace(min(residuals), max(residuals), 100)
residual_y = (1 / (residual_std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((residual_x - residual_mean) / residual_std)**2)

# Perform statistical tests
shapiro_stat, shapiro_p = stats.shapiro(residuals)
chi2_stat, chi2_p = stats.chisquare(f_obs=np.histogram(residuals, bins='auto', density=True)[0])

# Create the histogram plot with test results
ax3.hist(residuals, bins=15, density=True, alpha=0.7, color='green', label='Residual Distribution')
ax3.plot(residual_x, residual_y, 'r-', label=f'Normal Fit\nμ={residual_mean:.2e}\nσ={residual_std:.2e}')
ax3.set_title('Distribution of Residuals')
ax3.set_xlabel('Residual Value')
ax3.set_ylabel('Density')
ax3.grid(True, alpha=0.3)

# Add statistical test results to the legend
test_results = (f'Shapiro-Wilk test: p={shapiro_p:.3f}\n'
                f'Chi-square test: p={chi2_p:.3f}')
ax3.text(0.02, 0.98, test_results,
         transform=ax3.transAxes,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax3.legend()

plt.show() 