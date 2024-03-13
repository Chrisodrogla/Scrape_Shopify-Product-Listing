import os
import time
from selenium import webdriver
import pandas as pd
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, TimeoutException


from selenium.webdriver.chrome.options import Options
from datetime import datetime
import shutil

username = os.environ['TWTR_USER_NAME']
password = os.environ['TWTR_USER_PASS']
email = 'christopherchan645@gmail.com'

Login = "https://twitter.com/i/flow/login?newtwitter=true"

repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# Define the downloads directory within the repository
downloads_directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')

# Path to the downloaded extension .crx file
extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'
Login = "https://twitter.com/i/flow/login?newtwitter=true"

# Set up Chrome WebDriver with custom download directory
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_experimental_option("prefs", {
    "download.default_directory": downloads_directory,  # Set the download directory to the Downloads directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Define Chrome options
chrome_options = webdriver.ChromeOptions()

# Add the extension to Chrome options
chrome_options.add_extension(extension_path)

# Merge Chrome options
options.add_argument(f"--load-extension={extension_path}")

# Create WebDriver instance with merged Chrome options
driver = webdriver.Chrome(options=options)

driver.get(Login)

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

Myname = driver.find_element("xpath", """//*[@id="user-name"]""").text
print(Myname )

driver.quit()
#################################################################################################################################################################




# import os
# import time
# import datetime
# from selenium import webdriver
# import shutil
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import os
# from datetime import datetime

# # Get secrets from environment variables
# username = os.environ['TWTR_USER_NAME']
# password = os.environ['TWTR_USER_PASS']
# email = 'christopherchan645@gmail.com'

# # Define the repository directory
# repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# # Define the downloads directory within the repository
# downloads_directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')

# website = 'https://twitter.com/i/flow/login?newtwitter=true'

# # Define the path to the Chrome extension
# extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'

# Login = "https://twitter.com/i/flow/login?newtwitter=true"

# # Set up Chrome WebDriver with custom download directory
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920x1080")
# options.add_experimental_option("prefs", {
#     "download.default_directory": downloads_directory,  # Set the download directory to the Downloads directory
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# })

# # Define Chrome options
# chrome_options = webdriver.ChromeOptions()

# # Add the extension to Chrome options
# chrome_options.add_extension(extension_path)

# # Merge Chrome options
# options.add_argument(f"--load-extension={extension_path}")

# # Create WebDriver instance with merged Chrome options
# driver = webdriver.Chrome(options=options)

# driver.get(Login)


# username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input""")))

# username_input.send_keys(username)

# next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div""")))
# next_button.click()

# password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input""")))

# password_input.send_keys(password)

# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div""")))
# login_button.click()

# time.sleep(3)

# try:
    
#     email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//input[@autocomplete='email']""")))

#     email_input.send_keys(email)
#     time.sleep(3)

#     login_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div""")))
#     login_button2.click() 
# except:
#     pass

# Myname = driver.find_element("xpath", """//*[@id="user-name"]""").text
# print(Myname )

# driver.quit()
