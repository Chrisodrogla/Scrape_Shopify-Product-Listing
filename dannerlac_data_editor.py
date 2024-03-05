import os
import pandas as pd

# Define the directory path
directory = "Downloads/"

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

# Handle missing values by replacing them with empty strings
df['Style Number'] = df['Style Number'].fillna('')
df['Color Code'] = df['Color Code'].fillna('')
df['Size'] = df['Size'].fillna('')
df['Alt Size'] = df['Alt Size'].fillna('')

# Determine the maximum length of color codes
max_length = df['Color Code'].astype(str).map(len).max()

# Apply formatting to ensure all color codes have leading zeros to match the maximum length
df['Color Code'] = df['Color Code'].astype(str).apply(lambda x: '{:0>{width}}'.format(x, width=max_length))

# Add a new column "New SKU"
df['New SKU'] = df['Style Number'].astype(str) + "-" + df['Color Code'].astype(str) + "-" + df['Size'].astype(str) + df['Alt Size'].astype(str)

# Save the DataFrame as a CSV file with the Color Code column formatted
csv_file_path = os.path.splitext(excel_file_path)[0] + ".csv"
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
