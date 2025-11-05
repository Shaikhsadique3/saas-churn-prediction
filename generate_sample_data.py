import pandas as pd
import numpy as np

def balance_sample_data(input_file, output_file, total_users=500):
    # Load the data
    df = pd.read_csv(input_file)

    # Categorize users based on risk levels
    high_risk = df[df['churned'] == 1]
    low_risk = df[df['churned'] == 0]

    # Calculate medium-risk users (users with moderate activity)
    medium_risk = df[(df['churned'] == 0) & (df['logins_last30days'] > 5) & (df['logins_last30days'] <= 15)]

    # Ensure balanced sampling
    high_risk_sample = high_risk.sample(n=min(len(high_risk), total_users // 3), random_state=42)
    medium_risk_sample = medium_risk.sample(n=min(len(medium_risk), total_users // 3), random_state=42)
    low_risk_sample = low_risk.sample(n=min(len(low_risk), total_users - len(high_risk_sample) - len(medium_risk_sample)), random_state=42)

    # Combine all samples
    balanced_data = pd.concat([high_risk_sample, medium_risk_sample, low_risk_sample])

    # Shuffle the data
    balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save the balanced data to a new CSV file
    balanced_data.to_csv(output_file, index=False)

    print(f"Balanced sample data saved to {output_file} with {len(balanced_data)} users.")

# File paths
input_file = "c:\\Users\\Sadique\\Desktop\\ai model\\high_risk_sample_data.csv"
output_file = "c:\\Users\\Sadique\\Desktop\\ai model\\high_risk_sample_data.csv"

# Generate balanced sample data
balance_sample_data(input_file, output_file)