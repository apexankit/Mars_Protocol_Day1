import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- STEP 1: THE EXTRACTOR ---
def generate_mock_data():
    """
    Simulates fetching data from Aurum Wealth Database.
    Returns a raw, messy DataFrame.
    """
    print("[1/4] Generating Raw Data...")
    data = {
        'client_id': range(101, 111), # 10 Clients
        'client_name': ['Ankit', 'Rohan', 'Priya', 'Rahul', 'Sonal', 'Amit', 'Neha', 'Vikas', 'Pooja', 'Karan'],
        'investment_amount': [10000, '15,000', 12000, np.nan, 50000, 30000, '20000', 25000, 40000, 35000], # Dirty Data
        'risk_level': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'Medium']
    }
    return pd.DataFrame(data)

# --- STEP 2: THE CLEANER ---
def clean_data(df):
    """
    Takes messy data, fixes numbers, fills NaNs.
    """
    print("[2/4] Cleaning Data...")
    
    # Fix 'investment_amount' (Remove commas, convert to number)
    df['investment_amount'] = df['investment_amount'].astype(str).str.replace(',', '')
    df['investment_amount'] = pd.to_numeric(df['investment_amount'], errors='coerce')
    
    # Fill Missing Values with Median
    median_val = df['investment_amount'].median()
    df['investment_amount'] = df['investment_amount'].fillna(median_val)
    
    return df

# --- STEP 3: THE ANALYST ---
def analyze_data(df):
    """
    Calculates projected returns based on Risk Level.
    """
    print("[3/4] Analyzing Portfolio...")
    
    # Logic: High risk = 15%, Medium = 10%, Low = 6%
    conditions = [
        (df['risk_level'] == 'High'),
        (df['risk_level'] == 'Medium'),
        (df['risk_level'] == 'Low')
    ]
    values = [0.15, 0.10, 0.06]
    
    # Create 'expected_return_rate' column
    df['return_rate'] = np.select(conditions, values)
    
    # Vectorized Calculation (Day 3 Skill)
    df['projected_profit'] = df['investment_amount'] * df['return_rate']
    
    return df

# --- STEP 4: THE ARTIST ---
def generate_report(df):
    """
    Creates a summary chart and saves it.
    """
    print("[4/4] Generating Visual Report...")
    
    # Setup
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Plot: Total Investment by Risk Level
    # We use 'groupby' to aggregate data before plotting
    summary = df.groupby('risk_level')['projected_profit'].sum().reset_index()
    
    sns.barplot(data=summary, x='risk_level', y='projected_profit', palette='viridis')
    
    plt.title('Aurum Wealth: Projected Profit by Risk Profile', fontsize=14, fontweight='bold')
    plt.ylabel('Total Projected Profit (INR)')
    plt.xlabel('Risk Category')
    
    # Save
    filename = 'day6_Aurum_Risk_Analysis.png'
    plt.savefig(filename, dpi=300)
    print(f">> Report saved as: {filename}")
    
    # Verify file exists
    if os.path.exists(filename):
        print(">> SYSTEM SUCCESS: Pipeline Completed.")
    else:
        print(">> SYSTEM ERROR: File not found.")

# --- THE MASTER SWITCH ---
if __name__ == "__main__":
    # This is the sequence of automation
    raw_df = generate_mock_data()
    clean_df = clean_data(raw_df)
    final_df = analyze_data(clean_df)
    generate_report(final_df)
    
    print("\nTop 3 Clients by Projected Profit:")
    print(final_df.nlargest(3, 'projected_profit')[['client_name', 'projected_profit']])