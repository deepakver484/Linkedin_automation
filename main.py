from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import logging
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()  # Load the variables from .env file

# Retrieve username and password from environment variables
username = os.getenv('LINKEDIN_USERNAME')
password = os.getenv('LINKEDIN_PASSWORD')
print(username, password)


def login(username, password, cookies_file):
    # Initialize the Chrome WebDriver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        
#     driver = webdriver.Chrome(options=options)
    global driver
    driver = webdriver.Chrome(options = options)
    logging.info('chrome browser is opend')
    
    # Open LinkedIn login page
    url = "https://www.linkedin.com/login"
    driver.get(url)
    
    # Wait until the username and password fields are present
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    logging.info('username and password credential fedded')
    # Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    logging.info('logged in linkedin')
    # Wait until the page has loaded after login
    WebDriverWait(driver, 10).until(EC.url_changes(url))
    
     # Save cookies to a file
    cookies = driver.get_cookies()
    with open(cookies_file, 'w') as file:
        json.dump(cookies, file)
    
    logging.ingo(f"Cookies saved to {cookies_file}")
    
    # Close the browser
    driver.quit()
    # Print a success message
    logging.info(f'{username} successfully logged in')
