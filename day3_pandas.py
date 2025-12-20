import pandas as pd
import numpy as np
import time

print("--- SYSTEM: GENERATING 500,000 MOCK TRADES ---")
# 1. Create a massive dataset (Simulation of 5 Years of Aurum Wealth data)
# We create a DataFrame with 500,000 rows of random numbers
df = pd.DataFrame({
    'investment_id': range(1, 500001),
    'amount': np.random.randint(1000, 100000, 500000),  # Random amounts
    'interest_rate': np.random.uniform(0.05, 0.15, 500000) # Random rates (5% to 15%)
})

print(f"Data Loaded: {len(df)} rows ready for processing.\n")

# ==========================================
# METHOD 1: THE ROOKIE WAY (FOR LOOPS)
# Logic: Go row by row. Very slow.
# ==========================================
print("--- METHOD 1: LOOPING (The Old Way) ---")
start_time = time.time()

profit_loop = []
# iterrows is the enemy of speed. Never use it for math.
for index, row in df.iterrows():
    profit = row['amount'] * row['interest_rate']
    profit_loop.append(profit)

df['profit_loop'] = profit_loop
end_time = time.time()
loop_duration = end_time - start_time
print(f"Time taken by Loop: {loop_duration:.4f} seconds")


# ==========================================
# METHOD 2: THE DATA SCIENTIST WAY (VECTORIZATION)
# Logic: Multiply Column A * Column B instantly.
# ==========================================
print("\n--- METHOD 2: PANDAS VECTORIZATION (The Mars Protocol) ---")
start_time = time.time()

# This is the magic line. No loop. One command.
df['profit_vector'] = df['amount'] * df['interest_rate']

end_time = time.time()
vector_duration = end_time - start_time
print(f"Time taken by Vectorization: {vector_duration:.4f} seconds")

# ==========================================
# THE VERDICT
# ==========================================
speed_increase = loop_duration / vector_duration
print(f"\n--- RESULT ---")
print(f"Pandas was {speed_increase:.0f} times faster than the Loop.")

if speed_increase > 50:
    print("SUCCESS: You have successfully unlocked High-Speed Processing.")
else:
    print("WARNING: Something is checking. But it worked.")