import os
import json
import pandas as pd
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials
import gspread


# Step 1: Reading the JSON files and comparing the most recent and second most recent ones

def read_json_files(folder_path):
    json_files = os.listdir(folder_path)
    json_files.sort(reverse=True)  # Sort files by date, most recent first
    most_recent_file = json_files[0]
    second_most_recent_file = json_files[1]
    
    with open(os.path.join(folder_path, most_recent_file), 'r') as f:
        most_recent_data = json.load(f)
    
    with open(os.path.join(folder_path, second_most_recent_file), 'r') as f:
        second_most_recent_data = json.load(f)
    
    return most_recent_data, second_most_recent_data

# Step 2: Creating dataframes for "Followed Added", "Follow Removed", and "Overall"

def create_dataframes(most_recent_data, second_most_recent_data):
    most_recent_df = pd.DataFrame(most_recent_data)
    second_most_recent_df = pd.DataFrame(second_most_recent_data)
    
    followed_added_df = pd.DataFrame(columns=['User', 'User_Link'])
    followed_removed_df = pd.DataFrame(columns=['User', 'User_Link'])
    
    for index, row in second_most_recent_df.iterrows():
        if row['User'] not in most_recent_df['User'].values or row['User_Link'] not in most_recent_df['User_Link'].values:
            followed_removed_df = followed_removed_df.append(row, ignore_index=True)
    
    for index, row in most_recent_df.iterrows():
        if row['User'] not in second_most_recent_df['User'].values or row['User_Link'] not in second_most_recent_df['User_Link'].values:
            followed_added_df = followed_added_df.append(row, ignore_index=True)
    
    overall_df = most_recent_df.copy()
    
    return followed_added_df, followed_removed_df, overall_df

# Step 3: Integrating Google Sheets API to push data into Google Sheets

def push_to_google_sheets(dataframe, sheet_name, timestamp):
    # Step 3: Load Service Account Credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name('Twitter_Scraper/pro-course-388221-0a1e15f868e5.json')
    
    # Step 4: Authorize with Google Sheets API
    client = gspread.authorize(creds)
    
    # Step 5: Access the Google Sheet
    sheet = client.open("Your Google Sheet Name").worksheet(sheet_name)
    
    # Step 6: Convert DataFrame to List of Lists
    data = dataframe.values.tolist()
    
    # Step 7: Update the Google Sheet
    sheet.append_row(["Data for " + timestamp])  # Add timestamp as header
    sheet.append_rows(data)  # Append data to the Google Sheet

    pass

# Step 4: Automating the process

def main():
    folder_path = "Twitter_Scraper/Daily_Data"
    most_recent_data, second_most_recent_data = read_json_files(folder_path)
    followed_added_df, followed_removed_df, overall_df = create_dataframes(most_recent_data, second_most_recent_data)
    
    # Push data to Google Sheets
    timestamp = datetime.now().strftime("%m-%d-%Y at %I:%M %p CST")
    push_to_google_sheets(followed_added_df, "Follow Added", timestamp)
    push_to_google_sheets(followed_removed_df, "Follow Removed", timestamp)
    push_to_google_sheets(overall_df, "Overall", timestamp)

if __name__ == "__main__":
    main()
