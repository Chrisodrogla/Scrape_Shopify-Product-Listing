import os
import time
from selenium import webdriver

# Get secrets from environment variables
username = os.environ['D_USERNAME_SECRET']
password = os.environ['D_PASSWORD_SECRET']

website = 'https://lfi.elasticsuite.com/#builder,order'

# Set up Chrome WebDriver with custom download directory
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/temporary/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get(website)
time.sleep(5)

driver.find_element("xpath", """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/div[1]/div[2]/div/input""").send_keys(username)
driver.find_element("xpath", """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/div[2]/div[2]/div/input""").send_keys(password)
log = driver.find_element("xpath", """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/button""")
log.click()
time.sleep(2)
Shopnow=driver.find_element("xpath", """//*[@id="uniqName_10_0"]/div/div/div[4]/button[1]""").click()
time.sleep(2)
Menu =driver.find_element("xpath", """//*[@id="dijit__WidgetsInTemplateMixin_0"]/span""").click()
time.sleep(2)
third=driver.find_element("xpath", """//*[@id="dijit_MenuItem_6"]""").click()
time.sleep(2)
# fourth=driver.find_element("xpath", """//*[@id="uniqName_14_3"]/div[3]/span[2]""").click()
# time.sleep(10)
Fullcatalog=driver.find_element("xpath", """//*[@id="uniqName_14_3_full_catalog"]""").click()
time.sleep(10)
Allproducts=driver.find_element("xpath", """//*[@id="uniqName_14_3_all"]""").click()
time.sleep(10)
Export=driver.find_element("xpath", """//*[@id="uniqName_14_3"]/div[3]/span[2]/span""").click()

# Wait for download to complete (adjust time.sleep duration as needed)
time.sleep(30)

# # Move downloaded file to your GitHub repository directory
# temp_download_path = "/path/to/temporary/download/directory"
# downloaded_file = os.path.join(temp_download_path, "name_of_downloaded_file.csv")  # Adjust the file name as needed
# target_repo_path = "/path/to/your/repository"
#
# # Move the downloaded file to your GitHub repository directory
# os.rename(downloaded_file, os.path.join(target_repo_path, "name_of_downloaded_file.csv"))

# Close the WebDriver
driver.quit()





