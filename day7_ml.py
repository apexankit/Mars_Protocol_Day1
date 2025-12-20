import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("--- SYSTEM: INITIALIZING AI MODEL ---")

# 1. CREATE DATA (Experience vs Salary)
# This mimics real HR data
data = {
    'Years_Exp': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [40000, 45000, 55000, 60000, 70000, 80000, 85000, 100000, 110000, 120000]
}
df = pd.DataFrame(data)

# 2. SPLIT DATA
# We hide 20% of the data from the AI to test it later.
# X = Input (Years), y = Output (Salary)
X = df[['Years_Exp']]
y = df['Salary']

# train_test_split shuffles the data and splits it (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. TRAIN THE MODEL (The "Learning" Phase)
model = LinearRegression()
model.fit(X_train, y_train) 
print(">> AI Training Complete.")

# 4. PREDICT THE FUTURE
# Let's predict the salary for someone with 12 and 15 Years (Values not in our dataset)
future_years = pd.DataFrame({'Years_Exp': [12, 15]})
predictions = model.predict(future_years)

print("\n--- FORECAST REPORT ---")
print(f"Predicted Salary for 12 Years Exp: ₹{predictions[0]:,.2f}")
print(f"Predicted Salary for 15 Years Exp: ₹{predictions[1]:,.2f}")

# 5. VISUALIZE THE INTELLIGENCE
plt.figure(figsize=(10, 6))

# Plot the real data points
plt.scatter(X, y, color='blue', label='Actual Data')

# Plot the "Best Fit Line" (The AI's Logic)
plt.plot(X, model.predict(X), color='red', linewidth=2, label='AI Regression Line')

# Plot our future predictions
plt.scatter(future_years, predictions, color='green', s=100, label='Future Predictions', zorder=5)

plt.title('Salary Prediction Model (Linear Regression)', fontsize=14)
plt.xlabel('Years of Experience')
plt.ylabel('Salary (INR)')
plt.legend()
plt.grid(True)

plt.savefig('salary_prediction_model.png', dpi=300)
print(">> Graph saved: 'salary_prediction_model.png'")
plt.show()