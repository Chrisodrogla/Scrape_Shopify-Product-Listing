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
extension_path = 'Twitter_Scraper/JGEJDCDOEEABKLEPNKDBGLGCCJPDGPMF_1_8_2_0.crx'

options = webdriver.ChromeOptions()

# Add additional options to use the display created by Xvfb
options.add_argument("--headless")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--display=:99")  # Set display to Xvfb

# Add extension
options.add_extension(extension_path)

driver = webdriver.Chrome(options=options)
driver.get(Login)
time.sleep(5)

username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath",
                                                                                 """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input""")))

username_input.send_keys(username)

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                          """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div""")))
next_button.click()

password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath",
                                                                                 """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input""")))

password_input.send_keys(password)

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                           """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div""")))
login_button.click()

time.sleep(3)
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", """//input[@autocomplete='email']""")))

    email_input.send_keys(email)
    time.sleep(3)

    login_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath",
                                                                                """//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div""")))
    login_button2.click()
except:
    pass

time.sleep(10)






# Myname = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", """//*[@id="user-name""")))

# Myname1 = Myname.text
# print(Myname1)

element = driver.find_element("xpath", """//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/img""")
text = element.get_attribute('alt')

# Print the extracted text
print(text)





# time.sleep(4)
# main_twitter = "https://twitter.com/gotbit_io/following"
# driver.get(main_twitter)
# time.sleep(2)

# def scroll_to_bottom(driver):
#     # Get the height of the current page
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     while True:
#         # Scroll down to the bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#         # Wait for some time to load content
#         time.sleep(4)

#         # Calculate new height after scrolling
#         new_height = driver.execute_script("return document.body.scrollHeight")

#         # If the height doesn't change, then we've reached the bottom
#         if new_height == last_height:
#             break

#         last_height = new_height

# # Call the function to scroll down
# scroll_to_bottom(driver)

# User_Name = driver.find_elements("xpath", "//div[@class='user-item-text']/span[1]")
# User_Mail = driver.find_elements("xpath", "//div[@class='user-item-text']/span[2]")

# User_Links = driver.find_elements("xpath", "//a[@class='user-item-link']")

# # Concatenate the two lists
# Followers = zip(User_Name, User_Mail)

# following_list = []
# acc_link = []


# for user_name, user_mail in Followers:
#     formatted_user = f"{user_name.text} ({user_mail.text})"
#     following_list.append(formatted_user)


# for link in User_Links:
#     userl = link.get_attribute('href')
#     acc_link.append(userl)

# df = pd.DataFrame({'User': following_list, 'User_Link': acc_link})

# repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# # Define the downloads directory within the repository
# downloads_directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')


# # Specify the directory path
# directory = os.path.join(repo_directory, 'Twitter_Scraper/Daily_Data')

# # Create the directory if it doesn't exist
# os.makedirs(directory, exist_ok=True)

# # Generate filename based on current date and time
# current_time = datetime.now().strftime("%m-%d-%Y-%H-%M")
# filename = os.path.join(directory, f"{current_time}.json")

# # Save the DataFrame to JSON file with indentation and proper formatting
# df.to_json(filename, orient='records', indent=4)

# driver.quit()
