
import pandas as pd

# Load Dataset
df = pd.read_csv("dataset.csv")

# Explore Dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Handle Missing Values
df = df.dropna()   # Remove missing rows
# OR use: df.fillna(0, inplace=True)

# Filter Data (Example: Salary > 50000)
filtered_df = df[df["Salary"] > 50000]
print("\nFiltered Data:")
print(filtered_df)

# Sort Data by Salary
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted Data:")
print(sorted_df.head())

# Group By Department and Calculate Average Salary
grouped = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(grouped)

# Add New Calculated Column (Salary after 10% Bonus)
df["Bonus_Salary"] = df["Salary"] * 1.10

# Export Cleaned Data
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData analysis completed successfully!")
