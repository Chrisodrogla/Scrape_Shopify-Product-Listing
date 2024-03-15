import os
import json
import pandas as pd
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pytz

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
        if row['User'] not in most_recent_df['User'].values or row['User_Link'] not in most_recent_df[
            'User_Link'].values:
            followed_removed_df.loc[len(followed_removed_df)] = row

    for index, row in most_recent_df.iterrows():
        if row['User'] not in second_most_recent_df['User'].values or row['User_Link'] not in second_most_recent_df[
            'User_Link'].values:
            followed_added_df.loc[len(followed_added_df)] = row

    overall_df = most_recent_df.copy()

    return followed_added_df, followed_removed_df, overall_df


# Step 3: Integrating Google Sheets API to push data into Google Sheets

def push_to_google_sheets(dataframe, sheet_name, timestamp):
    # Load Service Account Credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name('Twitter_Scraper/pro-course-388221-0a1e15f868e5.json')

    # Authorize with Google Sheets API
    client = gspread.authorize(creds)

    # Access the Google Sheet
    sheet = client.open("X Twitter Gobit Hedge Fund").worksheet(sheet_name)

    # Convert DataFrame to List of Lists
    data = dataframe.values.tolist()

    # Update the Google Sheet
    if data:  # If data exists
        sheet.append_row(["Data for " + timestamp])  # Add timestamp as header
        sheet.append_rows(data)  # Append data to the Google Sheet
    else:  # If no data exists
        sheet.append_row(["Data for " + timestamp])  # Add timestamp as header
        sheet.append_row(["No User", "No Link"])  # Add "No User" and "No Link" to indicate no data

    pass


# Step 4: Automating the process

import pytz

def main():
    folder_path = "Twitter_Scraper/Daily_Data"
    most_recent_data, second_most_recent_data = read_json_files(folder_path)
    followed_added_df, followed_removed_df, overall_df = create_dataframes(most_recent_data, second_most_recent_data)

    # Push data to Google Sheets
    ct = pytz.timezone('America/Chicago')  # Central Time (CT) timezone
    timestamp = datetime.now(ct).strftime("%m-%d-%Y at %I:%M %p CST")
    
    # If there's no data, create a DataFrame with 'No User' and 'No Link'
    if followed_added_df.empty:
        followed_added_df = pd.DataFrame({'User': ['No User'], 'User_Link': ['No Link']})
    if followed_removed_df.empty:
        followed_removed_df = pd.DataFrame({'User': ['No User'], 'User_Link': ['No Link']})
    if overall_df.empty:
        overall_df = pd.DataFrame({'User': ['No User'], 'User_Link': ['No Link']})

    push_to_google_sheets(followed_added_df, "Follow Added", timestamp)
    push_to_google_sheets(followed_removed_df, "Follow Removed", timestamp)
    push_to_google_sheets(overall_df, "Overall", timestamp)


if __name__ == "__main__":
    main()
