import pandas as pd

# Define the path to the Excel file
excel_file_path = "Downloads/Downloads/Danner LaCrosse At Once.xlsx"

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Modify Quantity Available column to remove the sign
df['Quantity Available'] = df['Quantity Available'].str.replace('+', '')

# Add a new column "New SKU"
df['New SKU'] = df['Style Number'] + "-" + df['Color Code'] + "-" + df['Size'] + df['Alt Size']

# Save the DataFrame as a CSV file
csv_file_path = "Downloads/Downloads/Danner LaCrosse At Once.csv"
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
