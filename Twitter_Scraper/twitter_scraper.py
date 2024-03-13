import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Retrieving environment variables
username = os.environ.get('TWTR_USER_NAME')
password = os.environ.get('TWTR_USER_PASS')

# Define email and login URL
email = 'christopherchan645@gmail.com'
login_url = "https://twitter.com/i/flow/login?newtwitter=true"

# Path to Chrome extension
extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'

# Chrome options setup
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--display=:99")
options.add_extension(extension_path)

# Initialize Chrome driver
driver = webdriver.Chrome(options=options)

# Login to Twitter
driver.get(login_url)
time.sleep(5)

# Fill in username
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath",
                                                                                 """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input""")))
username_input.send_keys(username)

# Click next button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                          """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div""")))
next_button.click()

# Fill in password
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath",
                                                                                 """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input""")))
password_input.send_keys(password)

# Click login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                           """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div""")))
login_button.click()

time.sleep(3)
try:
    # Fill in email if prompted
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", """//input[@autocomplete='email']""")))
    email_input.send_keys(email)
    time.sleep(3)

    # Click login button if prompted
    login_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                                """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div""")))
    login_button2.click()
except:
    pass

time.sleep(10)

# Navigate to main Twitter following page
main_twitter = "https://twitter.com/gotbit_io/following"
driver.get(main_twitter)
time.sleep(2)

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_to_bottom(driver)

# Extracting user names, emails, and links
User_Name = driver.find_elements_by_xpath("//div[@class='user-item-text']/span[1]")
User_Mail = driver.find_elements_by_xpath("//div[@class='user-item-text']/span[2]")
User_Links = driver.find_elements_by_xpath("//a[@class='user-item-link']")

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

# Create DataFrame
df = pd.DataFrame({'User': following_list, 'User_Link': acc_link})

# Specify the directory path
directory = 'Twitter_Scraper/Daily_Data'

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Generate filename based on current date and time
current_time = time.strftime("%m-%d-%Y-%H-%M")
filename = os.path.join(directory, f"{current_time}.json")

# Save DataFrame to JSON file
df.to_json(filename, orient='records', indent=4)

# Quit driver
driver.quit()
