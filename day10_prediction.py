import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("--- SYSTEM: INITIALIZING ML PREDICTION ENGINE ---")

# 1. GENERATE MOCK BUSINESS DATA
# Scenario: Monthly Marketing Spend vs. Monthly Revenue
np.random.seed(42)
n_months = 100

# X = Marketing Spend (Input) - Random between 10k and 100k
marketing_spend = np.random.randint(10000, 100000, n_months)

# y = Revenue (Target) - Roughly 3x spend + some random noise
revenue = (marketing_spend * 3.5) + np.random.normal(0, 20000, n_months) + 50000

# Create DataFrame
df = pd.DataFrame({'Marketing_Spend': marketing_spend, 'Revenue': revenue})

print(f">> Data Generated: {df.shape[0]} months of records.")
print(df.head(3))

# 2. PREPARE DATA FOR AI (The "Feature Matrix")
# Scikit-Learn expects 'X' to be a 2D array (Matrix) and 'y' to be a 1D array (Vector)
X = df[['Marketing_Spend']] 
y = df['Revenue']

# 3. SPLIT DATA (The Exam Strategy)
# We hide 20% of data to test the model later. It cannot see this during training.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAIN THE MODEL (The "Learning" Phase)
model = LinearRegression()
model.fit(X_train, y_train)

print("\n--- TRAINING COMPLETE ---")
print(f"Intercept (Base Revenue without Ads): ₹{model.intercept_:.2f}")
print(f"Coefficient (Return on Ad Spend): {model.coef_[0]:.2f}")
print("(Interpretation: For every ₹1 spent on Ads, Revenue increases by this amount)")

# 5. MAKE PREDICTIONS (The Crystal Ball)
# Let's predict revenue for the Test Data
y_pred = model.predict(X_test)

# 6. EVALUATE PERFORMANCE
# R2 Score: How good is the model? (1.0 is perfect, 0.0 is useless)
score = r2_score(y_test, y_pred)
print(f"\n>> Model Accuracy (R2 Score): {score:.2f}")

# 7. VISUALIZE THE "GOD LINE"
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Revenue', data=df, color='blue', alpha=0.6, label='Actual Data')

# Plot the Regression Line
# We predict across the whole range of X to draw the line
line_X = np.linspace(df['Marketing_Spend'].min(), df['Marketing_Spend'].max(), 100).reshape(-1, 1)
line_y = model.predict(pd.DataFrame(line_X, columns=['Marketing_Spend']))
plt.plot(line_X, line_y, color='red', linewidth=2, label='Prediction Model')

plt.title(f'Marketing ROI Prediction (Accuracy: {score:.2f})')
plt.xlabel('Marketing Spend (₹)')
plt.ylabel('Revenue (₹)')
plt.legend()

# SAVE with correct prefix
plt.savefig('day10_revenue_prediction.png', dpi=300)
print("\n>> Plot saved as 'day10_revenue_prediction.png'")

# 8. REAL WORLD TEST
# "Dad asks: If I spend 75,000 next month, what happens?"
future_spend = pd.DataFrame({'Marketing_Spend': [75000]})
future_pred = model.predict(future_spend)
print(f"\n>> PREDICTION: If you spend ₹75,000, predicted revenue is ₹{future_pred[0]:,.2f}")