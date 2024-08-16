# plots.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import io

def ploting_of_data(data, login_data):
    fig, ax = plt.subplots(figsize=[10, 5])
    
    # Create horizontal bar plot
    bars = ax.barh(data.columns, data.loc['percentage'], color='green')

    # Add text labels and color coding based on percentage
    for bar, total_present, total, percent in zip(bars, data.loc['totalPresent'], data.loc['total'], data.loc['percentage']):
        if percent < 70:
            bar.set_color('red')
        elif percent < 75:
            bar.set_color('orange')
        elif percent < 80:
            bar.set_color('skyblue')
        
        # Adjust text position
        text_position = 102 if percent < 100 else percent + 2
        ax.text(text_position, bar.get_y() + bar.get_height() / 2, f'{total_present}/{total} = {percent:.2f}%', ha='left', va='center')

    # Add header and aggregate data
    ax.text(0.5, 1.18, login_data['email'], ha='center', va='center', transform=ax.transAxes, fontsize=14, fontweight='bold')
    ax.axvline(75, color='black', linestyle='--', alpha=0.5)

    tot_present = data.loc['totalPresent'].sum()
    tot_classes = data.loc['total'].sum()
    agg_percent = round((tot_present / tot_classes) * 100, 2)
    ax.text(0.5, 1.1, f"Total Attendance = {tot_present} / {tot_classes}", ha='center', va='center', transform=ax.transAxes, fontsize=14, fontweight='bold')
    ax.text(0.5, 1.04, f"Aggregate Percentage = {agg_percent}%", ha='center', va='center', transform=ax.transAxes, fontsize=14, fontweight='bold')

    # Set x-axis limits and grid
    ax.set_xlim(0, 100)
    ax.grid(True, alpha=0.3)
    
    # Adjust layout to avoid cropping
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    # Save plot to a BytesIO buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close(fig)
    
    return buf
