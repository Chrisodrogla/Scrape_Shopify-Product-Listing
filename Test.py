import time
import os
import requests  # Add this line
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup


def login_and_download(username, password):
    # Set the download directory
    download_dir = os.path.join(os.getcwd(), 'sample')  # 'sample' directory in the current working directory

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_dir}
    chrome_options.add_experimental_option('prefs', prefs)

    website = 'https://lfi.elasticsuite.com/#builder,order'

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the browser window
    driver.get(website)
    time.sleep(5)

    driver.find_element(By.XPATH, """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/div[1]/div[2]/div/input""").send_keys(username)
    driver.find_element(By.XPATH, """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/div[2]/div[2]/div/input""").send_keys(password)
    log = driver.find_element(By.XPATH, """//*[@id="elasticScramble_splash_login"]/div[1]/div/div/form/button""")
    log.click()
    time.sleep(2)

    # Explicit wait for Shopnow button to be clickable
    wait = WebDriverWait(driver, 10)
    Shopnow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniqName_10_0"]/div/div/div[4]/button[1]')))
    Shopnow.click()

    time.sleep(2)
    # Explicit wait for Menu button to be clickable
    Menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dijit__WidgetsInTemplateMixin_0"]/span')))
    Menu.click()

    time.sleep(2)

    # Explicit wait for the third menu item to be clickable
    third = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dijit_MenuItem_6"]')))
    third.click()

    time.sleep(2)

    Fullcatalog=driver.find_element(By.XPATH, """//*[@id="uniqName_14_3_full_catalog"]""")
    Fullcatalog.click()
    time.sleep(2)
    Allproducts=driver.find_element(By.XPATH, """//*[@id="uniqName_14_3_all"]""")
    Allproducts.click()
    time.sleep(2)

    # Explicit wait for the Export button to be clickable
    Export = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniqName_14_3"]/div[3]/span[2]/span')))
    Export.click()

    time.sleep(24)
    driver.quit()

# Example usage
username = "txfowlers"
password = "Txfowlers12!"
login_and_download(username, password)


def flxpoint():

    flx = 'https://app.flxpoint.com/sources/982516/integrations/1'
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get(flx)

    username2 = "christopherchan645@gmail.com"
    passw2 = "pqUaDaA4JU!ZP88"

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


    # Define the directory containing the files
    directory = os.path.join(os.getcwd(), 'sample')

    # Get a list of files in the directory
    files = os.listdir(directory)

    # Filter files to include only those with a .xlsx extension
    xlsx_files = [file for file in files if file.endswith('.xlsx')]

    # Upload each file
    for file_name in xlsx_files:
        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        # Your existing code to upload the file
        file_input = driver.find_element(By.XPATH, '//*[@id="primary-content"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/input')
        file_input.send_keys(file_path)

    time.sleep(1000)

flxpoint()