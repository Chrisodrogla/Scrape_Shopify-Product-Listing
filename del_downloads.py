import os
import shutil



def delete_from_downloads():
    # Define the path for the Downloads directory
    downloads_directory = "Downloads/"

    # Delete all CSV and XLSX files from Downloads
    for filename in os.listdir(downloads_directory):
        if filename.endswith(('.csv', '.xlsx')):
            file_path = os.path.join(downloads_directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted {filename} from Downloads")
            except Exception as e:
                print(f"Error deleting {filename} from Downloads: {e}")

# Call the function to copy files from Downloads to Archive


# Call the function to delete files from Downloads
delete_from_downloads()
