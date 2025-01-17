import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Create synthetic data from a normal distribution
np.random.seed(42)  # For reproducibility
true_mean = 2.5
true_std = 1.0
n_samples = 50
data = np.random.normal(true_mean, true_std, n_samples)

# Create figure and axes
fig = plt.figure(figsize=(15, 10))
gs = plt.GridSpec(2, 2, height_ratios=[1, 1])
ax1 = fig.add_subplot(gs[0, 0])  # Data and distribution
ax2 = fig.add_subplot(gs[0, 1], projection='3d')  # 3D likelihood surface
ax3 = fig.add_subplot(gs[1, 0])  # Log-likelihood vs mu
ax4 = fig.add_subplot(gs[1, 1])  # Log-likelihood vs sigma
plt.subplots_adjust(left=0.1, bottom=0.25, wspace=0.3, hspace=0.3)

# Create parameter ranges for visualization
mu_range = np.linspace(0, 5, 100)
sigma_range = np.linspace(0.1, 3, 100)

def log_likelihood(mu, sigma):
    """Calculate log likelihood for normal distribution"""
    return np.sum(norm.logpdf(data, mu, sigma))

def plot_likelihood():
    """Plot the data and current likelihood estimates"""
    # Clear previous plots
    ax1.clear()
    ax3.clear()
    ax4.clear()
    ax2.clear()
    
    # Get current parameter values
    current_mu = mu_slider.val
    current_sigma = sigma_slider.val
    
    # Plot 1: Data histogram and current distribution
    ax1.hist(data, bins=15, density=True, alpha=0.6, color='gray', label='Data')
    x = np.linspace(min(data)-1, max(data)+1, 100)
    y = norm.pdf(x, current_mu, current_sigma)
    ax1.plot(x, y, 'r-', lw=2, label=f'μ={current_mu:.2f}, σ={current_sigma:.2f}')
    ax1.plot(x, norm.pdf(x, true_mean, true_std), 'g--', lw=2, 
            label=f'True: μ={true_mean}, σ={true_std}')
    ax1.set_title('Data and Distribution')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: 3D log-likelihood surface
    MU, SIGMA = np.meshgrid(mu_range, sigma_range)
    Z = np.zeros_like(MU)
    for i in range(MU.shape[0]):
        for j in range(MU.shape[1]):
            Z[i,j] = log_likelihood(MU[i,j], SIGMA[i,j])
    
    ax2.plot_surface(MU, SIGMA, Z, cmap='viridis', alpha=0.8)
    ax2.scatter([current_mu], [current_sigma], [log_likelihood(current_mu, current_sigma)],
                color='red', s=100, marker='*')
    ax2.scatter([true_mean], [true_std], [log_likelihood(true_mean, true_std)],
                color='green', s=100, marker='*')
    ax2.set_xlabel('μ')
    ax2.set_ylabel('σ')
    ax2.set_zlabel('Log-Likelihood')
    ax2.set_title('Log-Likelihood Surface')
    ax2.view_init(elev=30, azim=45)

    # Plot 3: Log-likelihood vs mu (for current sigma)
    log_liks_mu = [log_likelihood(mu, current_sigma) for mu in mu_range]
    ax3.plot(mu_range, log_liks_mu, 'b-', lw=2)
    current_log_lik = log_likelihood(current_mu, current_sigma)
    ax3.plot(current_mu, current_log_lik, 'ro', markersize=10)
    ax3.axvline(true_mean, color='g', linestyle='--', alpha=0.5)
    ax3.set_title('Log-Likelihood vs. μ (for current σ)')
    ax3.set_xlabel('μ')
    ax3.set_ylabel('Log-Likelihood')
    ax3.grid(True, alpha=0.3)

    # Plot 4: Log-likelihood vs sigma (for current mu)
    log_liks_sigma = [log_likelihood(current_mu, sigma) for sigma in sigma_range]
    ax4.plot(sigma_range, log_liks_sigma, 'b-', lw=2)
    ax4.plot(current_sigma, current_log_lik, 'ro', markersize=10)
    ax4.axvline(true_std, color='g', linestyle='--', alpha=0.5)
    ax4.set_title('Log-Likelihood vs. σ (for current μ)')
    ax4.set_xlabel('σ')
    ax4.set_ylabel('Log-Likelihood')
    ax4.grid(True, alpha=0.3)

    # Add text showing current likelihood
    mle_mu = np.mean(data)
    mle_sigma = np.std(data)
    info_text = f"""
    Current Log-Likelihood: {current_log_lik:.2f}
    MLE Estimates:
    μ_MLE = {mle_mu:.2f}
    σ_MLE = {mle_sigma:.2f}
    """
    ax1.text(0.02, 0.98, info_text, transform=ax1.transAxes, 
             verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

# Create sliders
slider_color = 'lightgoldenrodyellow'
mu_slider_ax = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=slider_color)
sigma_slider_ax = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=slider_color)

mu_slider = Slider(mu_slider_ax, 'μ', 0.0, 5.0, valinit=np.mean(data))
sigma_slider = Slider(sigma_slider_ax, 'σ', 0.1, 3.0, valinit=np.std(data))

# Update function for both sliders
def update(val):
    plot_likelihood()
    fig.canvas.draw_idle()

# Register update function with each slider
mu_slider.on_changed(update)
sigma_slider.on_changed(update)

# Add explanation text
explanation = """
Maximum Likelihood Estimation (MLE):
• Finds parameters that maximize probability of observing the data
• For Gaussian: MLE of μ is sample mean, MLE of σ is sample standard deviation
• Log-likelihood used for numerical stability
• True parameters shown in green, current estimate in red
• 3D surface shows full parameter space
"""
plt.figtext(0.82, 0.15, explanation, fontsize=9, 
            bbox=dict(facecolor='white', alpha=0.8))

# Initial plot
plot_likelihood()

plt.show() 