import pandas as pd

# Read the Excel file
file_path = "Downloads/Downloads/Danner LaCrosse At Once.xlsx"
df = pd.read_excel(file_path)

# Modify Quantity Available column to remove the '+' sign and convert to numeric
df['Quantity Available'] = df['Quantity Available'].str.replace('+', '').astype(int)

# Add a new column named 'New SKU'
df['New SKU'] = df['Style Number'] + '-' + df['Color Code'] + '-' + df['Size'] + df['Alt Size']

# Save the modified DataFrame to a CSV file
csv_file_path = "Downloads/Downloads/Danner LaCrosse At Once.csv"
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
