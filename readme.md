# Linkedin Profile Scraper

## Objective -

Automate the login process to a LinkedIn account using cookies, without using the username and password.
Reuse the session to avoid re-logging in during subsequent script runs.
Develop a script to navigate to the user's LinkedIn profile and extract the following information:
Name
Secondary information (e.g., job title, location)
Followers count
Connections count
Most recent company

## Files Info


| **File Name**                                                                                                 | **Description**                              |
|---------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| [**main.py**](https://github.com/deepakver484/Linkedin_automation/main.py)                           | Main pipeline script for executing tasks.   |
| [**requirements.txt**](https://github.com/deepakver484/d2k-assignments/blob/deepak/requirements.txt)        | Lists Python dependencies for the project.  |



## Overview - 
This Python script automates LinkedIn login and profile data extraction using the Selenium WebDriver. It supports headless operation and manages session cookies for subsequent requests.

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

* Git
* Python (version 3.9 or higher)

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/yourusername/your-repository.git
    ```

2. Change to the directory
    ```sh
    cd your-repository
    ```

3. Create a virtual environment
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment

    On Windows:
    ```sh
    venv\Scripts\activate
    ```

    On macOS and Linux:
    ```sh
    source venv/bin/activate
    ```

5. Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```

6. **Create a `.env` file** in the root directory of your project.

7. **Add your LinkedIn credentials** to the `.env` file in the following format:

    ```plaintext
    LINKEDIN_USERNAME=your_linkedin_username
    LINKEDIN_PASSWORD=your_linkedin_password
    ```

    Replace `your_linkedin_username` and `your_linkedin_password` with your actual LinkedIn username and password.


## Main.py
This is the script in which all the logic and code write down for the scraping

## Functions

### `login(username, password, cookies_file)`

- **Arguments:** 
  - `username`: LinkedIn username
  - `password`: LinkedIn password
  - `cookies_file`: Path to the cookies file

- **Functionality:**
  - Configures Chrome WebDriver to run in headless mode
  - Logs into LinkedIn with the provided credentials
  - Saves session cookies to a file
  - Closes the browser

### `get_info(profile_url, cookies_file)`

- **Arguments:** 
  - `profile_url`: URL of the LinkedIn profile to scrape
  - `cookies_file`: Path to the cookies file

- **Functionality:**
  - Loads cookies from the file and adds them to the browser session
  - Opens the LinkedIn profile and scrapes information (name, followers, connections, job title, company name, location)
  - Returns the scraped information as a dictionary
 
    



