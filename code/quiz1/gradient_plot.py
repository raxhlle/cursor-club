import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Create figure with two subplots and space for sliders
fig = plt.figure(figsize=(15, 8))
plt.subplots_adjust(bottom=0.2)  # Make room for sliders

# First subplot: 3D surface
ax1 = fig.add_subplot(121, projection='3d')

# Create grid of points
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

# Define parabolic function f(x,y) = x² + y²
Z = X**2 + Y**2

def get_tangent_plane(x0, y0, z0):
    # Gradient at point (x0, y0)
    dx = 2 * x0
    dy = 2 * y0
    
    # Create a smaller grid around the point for the tangent plane
    span = 0.5
    xx = np.linspace(x0-span, x0+span, 10)
    yy = np.linspace(y0-span, y0+span, 10)
    XX, YY = np.meshgrid(xx, yy)
    
    # Tangent plane equation: z = z0 + dx(x-x0) + dy(y-y0)
    ZZ = z0 + dx*(XX-x0) + dy*(YY-y0)
    
    return XX, YY, ZZ

def update(val):
    # Get current slider values
    x_point = x_slider.val
    y_point = y_slider.val
    
    # Clear previous plots
    ax1.cla()
    ax2.cla()
    
    # Replot surface
    surface = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    
    # Calculate z value for point
    z_point = x_point**2 + y_point**2
    
    # Plot point on surface
    ax1.scatter([x_point], [y_point], [z_point], color='red', s=100)
    
    # Calculate and plot gradient vector at point
    gradient = np.array([2*x_point, 2*y_point, -1])
    gradient_norm = np.sqrt(np.sum(gradient**2))
    gradient = gradient / gradient_norm  # Normalize for visualization
    
    # Plot gradient vector on surface
    ax1.quiver(x_point, y_point, z_point,
               gradient[0], gradient[1], gradient[2],
               color='red', length=0.5, normalize=True)
    
    # Add tangent plane
    XX, YY, ZZ = get_tangent_plane(x_point, y_point, z_point)
    ax1.plot_surface(XX, YY, ZZ, alpha=0.3, color='red')
    
    # Customize 3D plot
    ax1.set_title('Parabolic Function with Point, Gradient, and Tangent Plane', fontsize=10)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_zlim(0, 8)
    
    # Replot gradient field
    U = 2 * X_coarse
    V = 2 * Y_coarse
    norm = np.sqrt(U**2 + V**2)
    U = U / norm
    V = V / norm
    
    ax2.quiver(X_coarse, Y_coarse, U, V, norm, cmap='viridis',
               angles='xy', scale_units='xy')
    
    # Add contour lines
    contours = ax2.contour(X, Y, Z, levels=levels, colors='k', alpha=0.3)
    ax2.clabel(contours, inline=True, fontsize=8)
    
    # Plot point on contour plot
    ax2.plot(x_point, y_point, 'ro')
    
    # Plot gradient vector on contour plot
    ax2.quiver(x_point, y_point, 2*x_point/gradient_norm, 2*y_point/gradient_norm,
               color='red', scale=5)
    
    # Customize gradient plot
    ax2.set_title(f'Gradient at ({x_point:.2f}, {y_point:.2f}): ({2*x_point:.2f}, {2*y_point:.2f})', 
                  fontsize=10)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-2, 2)
    
    fig.canvas.draw_idle()

# Initial plot of surface
surface = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
fig.colorbar(surface, ax=ax1, shrink=0.5, aspect=5)

# Second subplot: Gradient field
ax2 = fig.add_subplot(122)

# Create coarser grid for gradient arrows
x_coarse = np.linspace(-2, 2, 20)
y_coarse = np.linspace(-2, 2, 20)
X_coarse, Y_coarse = np.meshgrid(x_coarse, y_coarse)

# Add contour lines
levels = np.linspace(0, 8, 20)

# Create sliders
slider_ax_x = plt.axes([0.2, 0.1, 0.6, 0.03])
slider_ax_y = plt.axes([0.2, 0.05, 0.6, 0.03])

x_slider = Slider(slider_ax_x, 'X Position', -2, 2, valinit=0)
y_slider = Slider(slider_ax_y, 'Y Position', -2, 2, valinit=0)

# Connect sliders to update function
x_slider.on_changed(update)
y_slider.on_changed(update)

# Add text explanation
explanation = """
Gradient Properties:
• Points in direction of steepest increase
• Perpendicular to contour lines
• Magnitude proportional to slope
• Zero at critical points (minimum here at origin)
• Tangent plane shows local linearization
"""
plt.text(2.5, 0, explanation, fontsize=9, bbox=dict(facecolor='white', alpha=0.8))

# Initial update
update(None)

plt.show() 