import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("--- SYSTEM: INITIALIZING QUANT ENGINE ---")

# 1. GENERATE MOCK TIME SERIES DATA
# We create a date range for the year 2025
dates = pd.date_range(start='2025-01-01', periods=365, freq='D')

# Simulate a "Random Walk" for Gold Prices
# We start at 50,000 and add random daily fluctuations
np.random.seed(42) # Ensures we get the same random numbers every time
price_changes = np.random.normal(loc=10, scale=500, size=365) 
prices = 50000 + np.cumsum(price_changes)

# Create the DataFrame
df = pd.DataFrame({'Date': dates, 'Gold_Price': prices})

# 2. THE CRITICAL STEP: CONVERT & INDEX
# Python must treat 'Date' as a Time Object, not a String
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(f">> Data Loaded: {df.shape[0]} Days of Trading.")
print(df.head(3))

# 3. RESAMPLING (Aggregating Time)
# Let's see the Average Price per MONTH ('M')
monthly_avg = df['Gold_Price'].resample('M').mean()
print("\n--- MONTHLY AVERAGE PRICES ---")
print(monthly_avg.head())

# 4. ROLLING WINDOWS (The Moving Average)
# 20-Day SMA (Short Term Trend)
df['SMA_20'] = df['Gold_Price'].rolling(window=20).mean()

# 50-Day SMA (Long Term Trend)
df['SMA_50'] = df['Gold_Price'].rolling(window=50).mean()

# 5. GENERATE SIGNALS (The Algo)
# If SMA_20 > SMA_50, the trend is UP (Bullish)
df['Signal'] = np.where(df['SMA_20'] > df['SMA_50'], 'Bullish', 'Bearish')

print("\n--- LATEST MARKET STATUS ---")
print(df.tail(5))

# 6. VISUALIZATION (The Chart)
plt.figure(figsize=(12, 6))
sns.set_theme(style="darkgrid")

# Plot Actual Price (Light gray, to show noise)
plt.plot(df.index, df['Gold_Price'], label='Gold Price', color='lightgray', alpha=0.6)

# Plot SMAs (The Signals)
plt.plot(df.index, df['SMA_20'], label='20-Day SMA (Fast)', color='blue', linewidth=1.5)
plt.plot(df.index, df['SMA_50'], label='50-Day SMA (Slow)', color='red', linewidth=1.5, linestyle='--')

plt.title('Gold Price Algo Strategy: SMA Crossover', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

plt.savefig('gold_strategy.png', dpi=300)
print("\n>> Chart saved as 'gold_strategy.png'")
plt.show()