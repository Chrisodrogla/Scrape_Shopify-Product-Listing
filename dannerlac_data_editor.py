import pandas as pd
import os

# Get the current directory
current_directory = os.getcwd()

# Define the path to the Excel file
excel_file_path = os.path.join(current_directory, "Downloads/Downloads/Danner LaCrosse At Once.xlsx")

# Check if the file exists
if not os.path.exists(excel_file_path):
    print(f"Excel file '{excel_file_path}' not found.")
    exit(1)

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Modify Quantity Available column to remove the sign
df['Quantity Available'] = df['Quantity Available'].str.replace('+', '')

# Add a new column "New SKU"
df['New SKU'] = df['Style Number'] + "-" + df['Color Code'] + "-" + df['Size'] + df['Alt Size']

# Save the DataFrame as a CSV file
csv_file_path = os.path.join(current_directory, "Downloads/Downloads/Danner LaCrosse At Once.csv")
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
