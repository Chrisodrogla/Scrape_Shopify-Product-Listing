import pandas as pd
import os

# Get the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Construct the file path relative to the current working directory
file_path = os.path.join(current_dir, "Downloads", "Downloads", "Danner LaCrosse At Once.xlsx")

# Read the Excel file
df = pd.read_excel(file_path)

# Modify Quantity Available column to remove the '+' sign and convert to numeric
df['Quantity Available'] = df['Quantity Available'].str.replace('+', '').astype(int)

# Add a new column named 'New SKU'
df['New SKU'] = df['Style Number'] + '-' + df['Color Code'] + '-' + df['Size'] + df['Alt Size']

# Save the modified DataFrame to a CSV file
csv_file_path = os.path.join(current_dir, "Downloads", "Downloads", "Danner LaCrosse At Once.csv")
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
