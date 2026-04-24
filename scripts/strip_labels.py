import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Load the full dataset from your root
df = pd.read_csv('diabetes.csv')

# Split 80/20
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Save to the data folder for GitHub
train_df.to_csv('data/train.csv', index=False)
test_df.drop('Outcome', axis=1).to_csv('data/test_features.csv', index=False)

# Save the secret key locally (This file is gitignored)
test_df[['Outcome']].to_csv('test_labels_hidden.csv', index=False)

print("Data split complete.")
print("- Created data/train.csv (Shared with students)")
print("- Created data/test_features.csv (Shared with students)")
print("- Created test_labels_hidden.csv (KEEP THIS PRIVATE)")