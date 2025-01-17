import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
plt.subplots_adjust(bottom=0.2)  # Make room for slider

# Create a circle to show unit vectors
circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', alpha=0.5)
ax.add_artist(circle)

# Initial angle in degrees
initial_angle = 90

def update(angle_deg):
    ax.cla()  # Clear axis
    
    # Redraw circle
    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', alpha=0.5)
    ax.add_artist(circle)
    
    # Convert angle to radians
    angle_rad = np.radians(angle_deg)
    
    # Define vectors
    v1 = np.array([1.0, 0.0])  # First vector along x-axis
    v2 = np.array([np.cos(angle_rad), np.sin(angle_rad)])  # Second vector at angle
    
    # Calculate cosine similarity
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    
    # Plot vectors
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue',
             label=f'Vector 1 ({v1[0]:.1f}, {v1[1]:.1f})')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red',
             label=f'Vector 2 ({v2[0]:.1f}, {v2[1]:.1f})')
    
    # Add arc to show angle
    angle_range = np.linspace(0, angle_rad, 100)
    radius = 0.3
    ax.plot(radius * np.cos(angle_range), radius * np.sin(angle_range), 'g-', alpha=0.5)
    
    # Add text annotations
    ax.text(radius/2, radius/2, f'{angle_deg:.1f}°', fontsize=12)
    ax.text(0.5, -0.8, f'Cosine Similarity = {cos_sim:.3f}', fontsize=12,
           bbox=dict(facecolor='white', alpha=0.8))
    
    # Customize plot
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title('Cosine Similarity Visualization (Interactive)', fontsize=14)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.legend(loc='upper right')
    
    # Add explanation text
    explanation = """
    Cosine Similarity measures the cosine of the angle between two vectors:
    • Value of 1 means vectors point in same direction (0°)
    • Value of 0 means vectors are perpendicular (90°)
    • Value of -1 means vectors point in opposite directions (180°)
    """
    ax.text(-1.1, -1.1, explanation, fontsize=10, bbox=dict(facecolor='wheat', alpha=0.5))
    
    fig.canvas.draw_idle()

# Create slider axis
slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])
angle_slider = Slider(
    ax=slider_ax,
    label='Angle (degrees)',
    valmin=0,
    valmax=180,
    valinit=initial_angle,
    valstep=1
)

# Update function for slider
angle_slider.on_changed(update)

# Initial plot
update(initial_angle)

plt.show() 