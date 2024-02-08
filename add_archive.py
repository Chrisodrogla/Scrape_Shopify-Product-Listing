import os
import shutil

def copy_to_archive():
    # Define the paths for the Downloads and Archive directories
    downloads_directory = "Downloads/"
    archive_directory = "Archive/"

    # Ensure the Archive directory exists, create it if it doesn't
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)

    # Copy all CSV and XLSX files from Downloads to Archive
    for filename in os.listdir(downloads_directory):
        if filename.endswith(('.csv', '.xlsx')):
            source_file = os.path.join(downloads_directory, filename)
            destination_file = os.path.join(archive_directory, filename)
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied {filename} to Archive")
            except Exception as e:
                print(f"Error copying {filename}: {e}")


# Call the function to copy files from Downloads to Archive
copy_to_archive()

