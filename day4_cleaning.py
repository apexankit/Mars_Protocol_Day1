import pandas as pd
import numpy as np

print("--- SYSTEM: GENERATING DIRTY DATA ---")

# 1. Create a Messy Dataset (Simulating Bad Excel Entry)
data = {
    'client_name': ['Ankit', 'Rohan', 'Priya', 'Ankit', 'Rahul', 'Sonal'], # Duplicate 'Ankit'
    'deposit_date': ['2025-01-01', '01/02/2025', '2025-03-01', '2025-01-01', 'Invalid_Date', '2025-06-01'], # Mixed formats + Text
    'amount': [5000, 10000, np.nan, 5000, 7000, '12,000'], # NaN (Missing), String with comma
    'status': ['Active', 'Active', 'Closed', 'Active', 'Active', 'active'] # Case sensitivity issue ('active' vs 'Active')
}

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv") # Just kidding, using our manual data
df = pd.DataFrame(data)

print("\n--- 1. THE MESS (Raw Data) ---")
print(df)
print("\n--- INFO (Notice the Non-Null counts and Object types) ---")
print(df.info())

# ==========================================
# STEP 1: REMOVE DUPLICATES
# ==========================================
print("\n--- 2. REMOVING DUPLICATES ---")
# If Ankit appears twice with exact same data, remove the copy.
df = df.drop_duplicates()
print(f"Duplicates removed. Rows remaining: {len(df)}")

# ==========================================
# STEP 2: FIX NUMBERS (String -> Float)
# ==========================================
print("\n--- 3. CLEANING NUMBERS ---")
# '12,000' is text. We need to remove ',' and convert to float.
# If we don't do this, math operations will fail.
df['amount'] = df['amount'].astype(str).str.replace(',', '') # Remove comma
df['amount'] = pd.to_numeric(df['amount'], errors='coerce') # Convert to number. 'coerce' turns errors into NaN

# FILL MISSING VALUES (Imputation)
# Strategy: Fill missing amounts with the Median (safer than Mean)
median_val = df['amount'].median()
df['amount'] = df['amount'].fillna(median_val)
print("Amount column cleaned and NaNs filled with Median.")
print(df['amount'])

# ==========================================
# STEP 3: FIX DATES
# ==========================================
print("\n--- 4. STANDARDISING DATES ---")
# Convert everything to YYYY-MM-DD. Errors become NaT (Not a Time)
df['deposit_date'] = pd.to_datetime(df['deposit_date'], errors='coerce')

# Drop rows where Date is still unknown (if Date is critical)
df = df.dropna(subset=['deposit_date'])
print(df['deposit_date'])

# ==========================================
# STEP 4: STANDARDIZE TEXT
# ==========================================
print("\n--- 5. FIXING CATEGORIES ---")
# 'Active' and 'active' should be the same.
df['status'] = df['status'].str.title() # Capitalize first letter
print(df['status'].unique())

print("\n--- FINAL CLEAN DATASET ---")
print(df)