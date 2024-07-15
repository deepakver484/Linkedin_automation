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
from time import sleep


# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    handlers=[
        logging.StreamHandler()  # Log only to the console
    ]
)

# Load environment variables from the .env file
load_dotenv()  # Load the variables from .env file

# Retrieve username and password from environment variables
username = os.getenv('LINKEDIN_USERNAME')
password = os.getenv('LINKEDIN_PASSWORD')
logging.info('env file loaded properly')

def login(username, password, cookies_file):
    
    # driver = webdriver.Chrome(options=options)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")  
    # Initialize the Chrome WebDriver
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
    
    logging.info(f"Cookies saved to {cookies_file}")
    
    # Close the browser
    driver.quit()
    # Print a success message
    logging.info(f'{username} successfully logged in')

    return cookies_file



def get_info(profile_url, cookies_file):

    # driver = webdriver.Chrome(options=options)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options = options)
    driver.implicitly_wait(10)
    driver.get("https://www.linkedin.com/")
    if os.path.exists(cookies_file):
        logging.info(f"The cookies file '{cookies_file}' exists.")
    else:
        logging.info(f"The cookies file '{cookies_file}' does not exist.")
        cookies_file = login(username, password, cookies_file)
    with open(cookies_file, 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    # open the profile url
    driver.get(profile_url)
    logging.info('getting the url page after logging into the linkdin')
    try:
        name = driver.find_element(By.TAG_NAME, 'h1').text
    except:
        name = 'not found'
    try:
        followers = driver.find_element(By.XPATH, "//p[contains(@class, 'eemfwNAOAeLUgEQbAjMtPlVPpArRDuPBY pvs-header__optional-link text-body-small')]//span").text
    except:
        followers = 'not found'
    try:
        connections = driver.find_element(By.XPATH, "//ul[contains(@class, 'tqMrqKwsbRwhsuuMEHgTHkICClqlYeOdUgcyJvg sNBXKMUzFwekctRaCWOmGnJIwKlXwJsrfrvM')]").text

    except:
        connections = 'not found'
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    try:
        exp_element = driver.find_elements(By.XPATH, "//li[contains(@class, 'artdeco-list__item VFlaoWXigpPfgyfEgakujLQEATLGvsvNw aJBJPUQNbqXIxYgoChJLThEcxOeLRJBk')]")[0]
        try:
            job_title = exp_element.find_elements(By.TAG_NAME, 'span')[0].text
        except:
            job_title = 'not found'
        try:
            company_name = exp_element.find_elements(By.TAG_NAME, 'span')[3].text
        except:
            company_name = 'not found'
        try:
            location = exp_element.find_elements(By.TAG_NAME, 'span')[9].text
        except:
            location = 'not found'
            # returning info in the form of dictonary
        logging.info('data scraped successfully')
        logging.info({
            'name': name,
            'followers': followers,
            'connections': connections,
            'job_title':job_title,
            'company_name':company_name,
            'location':location
        })
        return {
            'name': name,
            'followers': followers,
            'connections': connections,
            'job_title':job_title,
            'company_name':company_name,
            'location':location
        }
    except:
        logging.info('not able to scrap data of the experience')
        logging.info({
            'name': name,
            'followers': followers,
            'connections': connections,
            'job_title':'not found',
            'company_name':'not found',
            'location':'not found'
        })
        return {
            'name': name,
            'followers': followers,
            'connections': connections,
            'job_title':'not found',
            'company_name':'not found',
            'location':'not found'
        }
    

get_info('https://www.linkedin.com/in/deepakkumarverma484/', 'cookies.json')
        