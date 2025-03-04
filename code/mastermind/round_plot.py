import matplotlib.pyplot as plt
import numpy as np

# Data from the image
rounds = [0, 1, 2, 3, 4]
codes_remaining = [1296, 216, 36, 6, 1]
entropy = [10.34, 7.75, 5.2, 2.58, 0]

# Create figure without extra height now that table is inside
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(111)

# Plot N (Possible Codes Remaining) on left y-axis
color1 = '#1f77b4'  # Blue color
ln1 = ax1.plot(rounds, codes_remaining, color=color1, marker='o', linewidth=2, 
               markersize=8, label='Possible Codes (N)')
ax1.set_xlabel('Round', fontsize=14, weight='bold')
ax1.set_ylabel('Possible Codes Remaining (N)', color=color1, fontsize=14, weight='bold')
ax1.tick_params(axis='y', labelcolor=color1)

# Set integer ticks for x-axis
ax1.set_xticks(rounds)
ax1.set_xticklabels(rounds)

# Create second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot Entropy on right y-axis
color2 = '#ff7f0e'  # Orange color
ln2 = ax2.plot(rounds, entropy, color=color2, marker='s', linewidth=2, 
               markersize=8, label='Entropy (H)')
ax2.set_ylabel('Entropy (H) (log₂(N))', color=color2, fontsize=14, weight='bold')
ax2.tick_params(axis='y', labelcolor=color2)

# Add title
ax1.set_title('Possible Codes and Entropy vs Round', fontsize=16, pad=20, weight='bold')

# Add grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Add padding to y-axis ranges
y1_min, y1_max = min(codes_remaining), max(codes_remaining)
y2_min, y2_max = min(entropy), max(entropy)

padding1 = (y1_max - y1_min) * 0.15
padding2 = (y2_max - y2_min) * 0.15

ax1.set_ylim(y1_min - padding1, y1_max + padding1)
ax2.set_ylim(y2_min - padding2, y2_max + padding2)

# Add data point labels for both metrics
for x, y1, y2 in zip(rounds, codes_remaining, entropy):
    ax1.annotate(f'N={y1}', 
                (x, y1), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center',
                color=color1,
                fontsize=11,
                weight='bold')
    ax2.annotate(f'H={y2}', 
                (x, y2), 
                textcoords="offset points", 
                xytext=(0,-20), 
                ha='center',
                color=color2,
                fontsize=11,
                weight='bold')

# Combine legends from both axes
lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper right', fontsize=14, prop={'size': 14, 'weight': 'bold'})

# Add table inside the plot
table_data = [
    ['Round', 'N', 'H'],  # Simplified headers
    *[[str(r), str(n), str(h)] for r, n, h in zip(rounds, codes_remaining, entropy)]
]

# Position table lower and to the right, with narrower columns
table = ax1.table(
    cellText=table_data,
    loc='center',
    cellLoc='center',
    bbox=[0.65, 0.45, 0.3, 0.25],  # Moved right (0.65) and made narrower (0.3 width)
    colWidths=[0.08, 0.08, 0.08]  # Specify narrow widths for each column
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(11)  # Slightly smaller font
for cell in table._cells:
    table._cells[cell].set_text_props(weight='bold')
    table._cells[cell].set_edgecolor('black')
    if cell[1] == 0:  # Header column
        table._cells[cell].set_facecolor('#e6e6e6')
    # Make cells more compact
    table._cells[cell].set_height(0.15)

# Adjust layout with better margins
plt.subplots_adjust(top=0.9, bottom=0.12, left=0.1, right=0.9)

# Save the plot
plt.savefig('round_plot.png', bbox_inches='tight', dpi=300)
plt.show() 