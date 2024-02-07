import os
import time
from selenium import webdriver
import shutil

# Get secrets from environment variables
username = os.environ['D_USERNAME_SECRET']
password = os.environ['D_PASSWORD_SECRET']

# Define the repository directory
repo_directory = os.getcwd()  # This gets the current working directory (your repository directory)

# Define the downloads directory within the repository
downloads_directory = os.path.join(repo_directory, 'Downloads')

# Ensure the Downloads directory exists, create it if it doesn't
if not os.path.exists(downloads_directory):
    os.makedirs(downloads_directory)

website = 'https://lfi.elasticsuite.com/#builder,order'

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

Fullcatalog=driver.find_element("xpath", """//*[@id="uniqName_14_3_full_catalog"]""").click()
time.sleep(10)
Allproducts=driver.find_element("xpath", """//*[@id="uniqName_14_3_all"]""").click()
time.sleep(10)
Export=driver.find_element("xpath", """//*[@id="uniqName_14_3"]/div[3]/span[2]/span""").click()

time.sleep(100)

# Move the downloaded file to the Downloads directory
for filename in os.listdir(downloads_directory):
    if filename.endswith('.xlsx'):  # Modify this condition based on the file type you're downloading
        source_file = os.path.join(downloads_directory, filename)
        destination_file = os.path.join(downloads_directory, 'Downloads', filename)
        shutil.move(source_file, destination_file)

driver.quit()
