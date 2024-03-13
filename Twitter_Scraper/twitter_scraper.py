import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Get secrets from environment variables
username = os.environ.get('TWTR_USER_NAME')
password = os.environ.get('TWTR_USER_PASS')
email = 'christopherchan645@gmail.com'

# Define the repository directory
repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# Define the downloads directory within the repository
downloads_directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')

# Define the path to the Chrome extension
extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'

# Set up Chrome WebDriver with custom download directory
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--disable-dev-tools")   # Disable developer tools
options.add_experimental_option("prefs", {
    "download.default_directory": downloads_directory,  
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Create WebDriver instance with Chrome options
driver = webdriver.Chrome(options=options)

# Define URLs
login_url = "https://twitter.com/login"
main_twitter_url = "https://twitter.com/gotbit_io/following"

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

# Function to login to Twitter
def login_to_twitter():
    driver.get(login_url)

    try:
        # Wait for username input to load
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//input[@name='session[username_or_email]']")))
        username_input.send_keys(username)

        # Wait for next button to be clickable and click it
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@data-testid='LoginForm_Login_Button']")))
        next_button.click()

        # Wait for password input to load
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//input[@name='session[password]']")))
        password_input.send_keys(password)

        # Wait for login button to be clickable and click it
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@data-testid='LoginForm_Login_Button']")))
        login_button.click()

        time.sleep(3)  # Adding a sleep for page to load
    except Exception as e:
        print("Exception occurred during login:", e)

# Function to scrape following list
def scrape_following():
    driver.get(main_twitter_url)
    time.sleep(5)  # Adding a sleep for page to load

    scroll_to_bottom(driver)

    # Find user names, emails, and links
    user_names = driver.find_elements_by_xpath("//div[@class='user-item-text']/span[1]")
    user_mails = driver.find_elements_by_xpath("//div[@class='user-item-text']/span[2]")
    user_links = driver.find_elements_by_xpath("//a[@class='user-item-link']")

    following_list = []
    acc_link = []

    for user_name, user_mail in zip(user_names, user_mails):
        formatted_user = f"{user_name.text} ({user_mail.text})"
        following_list.append(formatted_user)

    for link in user_links:
        user_link = link.get_attribute('href')
        acc_link.append(user_link)

    df = pd.DataFrame({'User': following_list, 'User_Link': acc_link})

    return df

# Function to save data to JSON file
def save_to_json(df):
    directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Generate filename based on current date and time
    current_time = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M")
    filename = os.path.join(directory, f"{current_time}.json")

    # Save the DataFrame to JSON file with indentation and proper formatting
    df.to_json(filename, orient='records', indent=4)
    print(f"Data saved to {filename}")

# Main function
def main():
    try:
        login_to_twitter()
        df = scrape_following()
        save_to_json(df)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
