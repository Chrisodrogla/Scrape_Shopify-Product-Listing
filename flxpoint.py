import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil

# Get secrets from environment variables
username2 = os.environ['FLX_USERNAME_SECRET']
passw2 = os.environ['FLX_PASSWORD_SECRET']


flx = 'https://app.flxpoint.com/sources/982516/integrations/1'

# Set up Chrome WebDriver with custom download directory
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")


driver = webdriver.Chrome(options=options)
driver.get(flx)
time.sleep(5)

driver.find_element("xpath", """//*[@id="app"]/div[1]/div/form/div[1]/div/input""").send_keys(username2)
time.sleep(2)
driver.find_element("xpath", """//*[@id="app"]/div[1]/div/form/div[2]/div/input""").send_keys(passw2)

log = driver.find_element("xpath", """//*[@id="app"]/div[1]/div/form/button""")
log.click()
time.sleep(2)

# Wait until the Manual button is clickable
manual_button_xpath = '//*[@id="primary-content"]/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[6]/button'
manual_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, manual_button_xpath)))
manual_button.click()

time.sleep(3)

directory = "Downloads/Downloads/"

# Find the Excel file with the end name ".xlsx"
excel_file_path = None
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        excel_file_path = os.path.join(directory, filename)
        break


    # Your existing code to upload the file
    file_input = driver.find_element(By.XPATH,
                                     '//*[@id="primary-content"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/input')
    file_input.send_keys(excel_file_path)

time.sleep(50)
driver.quit()