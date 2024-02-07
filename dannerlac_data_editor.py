import pandas as pd
import os
import shutil

# Define the repository directory
repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# Define the downloads directory within the repository
downloads_directory = os.path.join(repo_directory, 'Downloads')

# Ensure the Downloads directory exists, create it if it doesn't
if not os.path.exists(downloads_directory):
    os.makedirs(downloads_directory)

# Move the downloaded file to the Downloads directory
for filename in os.listdir(repo_directory):  # Assuming the downloaded file is in the repository directory
    if filename.endswith('.xlsx'):  # Modify this condition based on the file type you're downloading
        source_file = os.path.join(repo_directory, filename)
        destination_file = os.path.join(downloads_directory, filename)
        shutil.move(source_file, destination_file)

# Construct the file path relative to the downloads directory
file_path = os.path.join(downloads_directory, 'Danner LaCrosse At Once.xlsx')

# Read the Excel file
df = pd.read_excel(file_path)

# Modify Quantity Available column to remove the '+' sign and convert to numeric
df['Quantity Available'] = df['Quantity Available'].str.replace('+', '').astype(int)

# Add a new column named 'New SKU'
df['New SKU'] = df['Style Number'] + '-' + df['Color Code'] + '-' + df['Size'] + df['Alt Size']

# Save the modified DataFrame to a CSV file
csv_file_path = os.path.join(downloads_directory, 'Danner LaCrosse At Once.csv')
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
