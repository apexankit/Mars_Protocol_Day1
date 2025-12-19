import sqlite3
import pandas as pd

# 1. Setup the "In-Memory" Database
conn = sqlite3.connect(':memory:')

# 2. Create a Dummy Table
conn.execute('''
 CREATE TABLE employees (
 id INTEGER PRIMARY KEY,
 name TEXT,
 department TEXT,
 salary INTEGER
 )
''')

# 3. Insert Data (Notice duplicates in Sales to test Ranking)
data = [
 (1, 'Ankit', 'IT', 80000),
 (2, 'Rahul', 'IT', 90000),
 (3, 'Priya', 'IT', 80000),
 (4, 'Amit', 'Sales', 50000),
 (5, 'Sneha', 'Sales', 60000),
 (6, 'Vikram', 'Sales', 60000)
]
conn.executemany('INSERT INTO employees VALUES (?,?,?,?)', data)

print("--- SQL LAB INITIALIZED ---\n")

# --- CHALLENGE 1: RANKING ---
# Question: Rank employees by salary inside their department.
# If salaries are same, give same rank (Dense Rank).
sql_rank = '''
 SELECT 
 name, 
 department, 
 salary,
 DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
 FROM employees
'''
print("--- Output: Dense Rank ---")
print(pd.read_sql_query(sql_rank, conn))
print("\n")

# --- CHALLENGE 2: GROWTH (LAG) ---
# Question: Who earns more than the person listed just below them?
sql_lag = '''
 SELECT 
 name,
 salary,
 LAG(salary, 1, 0) OVER (ORDER BY salary) as previous_person_salary,
 (salary - LAG(salary, 1, 0) OVER (ORDER BY salary)) as salary_diff
 FROM employees
'''
print("--- Output: Lead/Lag Analysis ---")
print(pd.read_sql_query(sql_lag, conn))

# Get CTE with High earners
sql_cte = '''
with HighEarners AS (
    Select * from employees
    where salary > 75000 )
Select * from HighEarners;
'''

print("\n--- Output: CTE High Earners ---")
print(pd.read_sql_query(sql_cte, conn))

# 4. Close the connection
conn.close()