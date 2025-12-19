import pandas as pd
import numpy as np

def create_data():
    # Create a DataFrame with sample data
    data = {
        'Name'  : ['Ankit', 'Recruiter'],
        'Role'  : ['Candidate', 'Hiring Manager'],
        'Status': ['Ready', 'Impressed']
    }
    df = pd.DataFrame(data)
    return df
if __name__ == "__main__":
    print("---Mars Protocol Initiated---")
    df_result = create_data()
    print(df_result)
    print("---Environment Setup Complete---")

    