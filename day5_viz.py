import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. SETUP THE STYLE (The "Professional" Look)
# seaborn has built-in themes. 'whitegrid' looks clean for finance.
sns.set_theme(style="whitegrid")

print("--- SYSTEM: GENERATING VISUALIZATIONS ---")

# 2. CREATE MOCK DATA (Aurum Wealth Client Portfolio)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Equity': [100000, 105000, 102000, 108000, 112000, 115000], # Upward trend
    'Gold': [50000, 51000, 50500, 52000, 52500, 53000],        # Steady
    'Bonds': [30000, 30100, 30200, 30300, 30400, 30500]        # Flat
}
df = pd.DataFrame(data)

# Reshape data for plotting (Wide to Long format) - Advanced Pandas Trick
# This makes it easier for Seaborn to plot multiple lines at once.
df_long = df.melt('Month', var_name='Asset_Class', value_name='Value')

# ==========================================
# CHART 1: PORTFOLIO GROWTH (Line Chart)
# Objective: Show the client they are making money.
# ==========================================
plt.figure(figsize=(10, 6)) # Set size (Width, Height)

# The Magic Command
sns.lineplot(data=df_long, x='Month', y='Value', hue='Asset_Class', marker='o', linewidth=2.5)

plt.title('Aurum Wealth: Portfolio Growth (H1 2025)', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Portfolio Value (INR)')
plt.legend(title='Asset Type')

# CRITICAL STEP: SAVE THE CHART
# In automation, we don't 'show' charts, we save them to send in emails.
plt.savefig('growth_chart.png', dpi=300) 
print(">> Success: 'growth_chart.png' saved to your folder.")

# ==========================================
# CHART 2: ASSET ALLOCATION (Bar Chart)
# Objective: Show where their money is right now (June).
# ==========================================
# Get only June data
june_data = df_long[df_long['Month'] == 'Jun']

plt.figure(figsize=(8, 6))
# A distinct color palette (Pastel is classy)
colors = sns.color_palette('pastel')

sns.barplot(data=june_data, x='Asset_Class', y='Value', palette=colors)

plt.title('Current Asset Allocation (June)', fontsize=14)
plt.ylabel('Value (INR)')

# Add actual numbers on top of bars (The "Data Analyst" touch)
for index, row in enumerate(june_data.itertuples()):
    # logic to place text: x_position, y_height, text_value
    plt.text(index, row.Value + 1000, f"₹{row.Value}", color='black', ha="center")

plt.savefig('allocation_chart.png', dpi=300)
print(">> Success: 'allocation_chart.png' saved to your folder.")

# Show them on screen now
plt.show()
