import os
import time
import datetime
from selenium import webdriver
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
from datetime import datetime

# Get secrets from environment variables
username = os.environ['TWTR_USER_NAME']
password = os.environ['TWTR_USER_PASS']
email = 'christopherchan645@gmail.com'

# Define the repository directory
repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)



website = 'https://twitter.com/i/flow/login?newtwitter=true'

# Define the path to the Chrome extension
extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'

# Set up Chrome WebDriver with custom download directory and extension
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--load-extension={extension_path}")  # Add the extension

driver = webdriver.Chrome(options=options)
driver.get(website)
time.sleep(5)


username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input""")))

username_input.send_keys(username)

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div""")))
next_button.click()

password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input""")))

password_input.send_keys(password)

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div""")))
login_button.click()

time.sleep(3)

try:
    
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//input[@autocomplete='email']""")))

    email_input.send_keys(email)
    time.sleep(3)

    login_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div""")))
    login_button2.click() 
except:
    pass

time.sleep(4)
main_twitter = "https://twitter.com/gotbit_io/following"
driver.get(main_twitter)
time.sleep(10)

def scroll_to_bottom(driver):
    # Get the height of the current page
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for some time to load content
        time.sleep(10)

        # Calculate new height after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")

        # If the height doesn't change, then we've reached the bottom
        if new_height == last_height:
            break

        last_height = new_height

# Call the function to scroll down
scroll_to_bottom(driver)


User_Name = driver.find_elements("xpath", "//div[@class='user-item-text']/span[1]")
User_Mail = driver.find_elements("xpath", "//div[@class='user-item-text']/span[2]")

User_Links = driver.find_elements("xpath", "//a[@class='user-item-link']")

# Concatenate the two lists
Followers = zip(User_Name, User_Mail)

following_list = []
acc_link = []


for user_name, user_mail in Followers:
    formatted_user = f"{user_name.text} ({user_mail.text})"
    following_list.append(formatted_user)


for link in User_Links:
    userl = link.get_attribute('href')
    acc_link.append(userl)

df = pd.DataFrame({'User': following_list, 'User_Link': acc_link})

directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')


# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Generate filename based on current date and time
current_time = datetime.now().strftime("%m-%d-%Y-%H-%M")
filename = os.path.join(directory, f"{current_time}.json")

# Save the DataFrame to JSON file with indentation and proper formatting
df.to_json(filename, orient='records', indent=4)

driver.quit()
