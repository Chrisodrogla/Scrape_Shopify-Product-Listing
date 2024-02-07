import os
import pandas as pd

# Define the directory path
directory = "Downloads/Downloads/"

# Find the Excel file with the end name ".xlsx"
excel_file_path = None
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        excel_file_path = os.path.join(directory, filename)
        break

# If no Excel file is found, exit the script
if excel_file_path is None:
    print("No Excel file found in the directory.")
    exit()

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Modify Quantity Available column to remove the sign
df['Quantity Available'] = df['Quantity Available'].astype(str).str.replace('+', '')

# Add a new column "New SKU"
df['New SKU'] = df['Style Number'].astype(str) + "-" + df['Color Code'].astype(str) + "-" + df['Size'].astype(str) + df['Alt Size'].astype(str)

# Save the DataFrame as a CSV file
csv_file_path = os.path.splitext(excel_file_path)[0] + ".csv"
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
