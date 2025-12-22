import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("--- SYSTEM: GENERATING COMPLEX MOCK DATA ---")

# 1. GENERATE MOCK DATA (More complex than before)
data = {
    'Transaction_ID': range(1001, 1021),
    'Client_Name': ['Ankit', 'Rohan', 'Priya', 'Ankit', 'Rohan', 'Amit', 'Priya', 'Neha', 'Ankit', 'Sonal', 
                    'Amit', 'Rohan', 'Priya', 'Neha', 'Sonal', 'Ankit', 'Amit', 'Rohan', 'Priya', 'Neha'],
    'City': ['Korba', 'Raipur', 'Bilaspur', 'Korba', 'Raipur', 'Durg', 'Bilaspur', 'Korba', 'Korba', 'Raipur',
             'Durg', 'Raipur', 'Bilaspur', 'Korba', 'Raipur', 'Korba', 'Durg', 'Raipur', 'Bilaspur', 'Korba'],
    'Asset_Class': ['Gold', 'Equity', 'Gold', 'Mutual Fund', 'Equity', 'Gold', 'Equity', 'Mutual Fund', 'Gold', 'Equity',
                    'Mutual Fund', 'Gold', 'Equity', 'Gold', 'Mutual Fund', 'Equity', 'Gold', 'Equity', 'Mutual Fund', 'Equity'],
    'Amount': [50000, 12000, 45000, 10000, 15000, 60000, 11000, 8000, 52000, 13000,
               9000, 48000, 11500, 51000, 7500, 10500, 58000, 14000, 8200, 12500],
    'Status': ['Completed', 'Completed', 'Pending', 'Completed', 'Completed', 'Failed', 'Completed', 'Completed', 'Completed', 'Completed',
               'Completed', 'Completed', 'Completed', 'Pending', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed']
}

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv") # Just kidding
df = pd.DataFrame(data)

print(f"Data Loaded: {df.shape[0]} transactions.")

# ==========================================
# SKILL 1: THE GROUPBY (The "Pivot Table" of Code)
# Question: How much total money has each Client invested?
# ==========================================
print("\n--- 1. TOTAL PORTFOLIO BY CLIENT ---")
client_total = df.groupby('Client_Name')['Amount'].sum().sort_values(ascending=False)
print(client_total)

# ==========================================
# SKILL 2: MULTI-GROUPING
# Question: How much is invested in Gold vs Equity in EACH City?
# ==========================================
print("\n--- 2. CITY WISE ASSET DISTRIBUTION ---")
city_asset = df.groupby(['City', 'Asset_Class'])['Amount'].sum()
print(city_asset)

# ==========================================
# SKILL 3: THE PIVOT TABLE (For Heatmaps)
# This creates a matrix: Rows=City, Cols=Asset_Class, Values=Total Amount
# ==========================================
print("\n--- 3. PIVOT TABLE STRUCTURE ---")
pivot_df = df.pivot_table(values='Amount', index='City', columns='Asset_Class', aggfunc='sum', fill_value=0)
print(pivot_df)

# ==========================================
# SKILL 4: VISUALIZING THE PIVOT (Heatmap)
# This is how you spot trends instantly.
# ==========================================
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_df, annot=True, fmt="d", cmap="YlGnBu") # YlGnBu = Yellow Green Blue
plt.title('Investment Heatmap: City vs Asset Class')
plt.savefig('heatmap_analysis.png', dpi=300)
print("\n>> Heatmap saved as 'heatmap_analysis.png'")

# ==========================================
# SKILL 5: COMPLEX FILTERING
# Question: Show me only "Completed" transactions greater than 10,000
# ==========================================
print("\n--- 4. HIGH VALUE COMPLETED TRANSACTIONS ---")
high_value = df[ (df['Status'] == 'Completed') & (df['Amount'] > 10000) ]
print(high_value[['Client_Name', 'Amount', 'Status']])