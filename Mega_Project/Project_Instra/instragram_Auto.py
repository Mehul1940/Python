import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("https://www.instagram.com/")

# Wait for the page to load
time.sleep(2)

# Enter username and password (replace with your own credentials)
driver.find_element(By.NAME, "username").send_keys("Your-email")
driver.find_element(By.NAME, "password").send_keys("Your-password")

# Wait for 2 seconds before clicking login
time.sleep(2)

# Click the login button
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()

# Wait for 2 seconds after login
time.sleep(2)

# Skip the "Save your login info?" popup (click "Not Now")
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

# Wait for 2 seconds after handling the "Not Now" button
time.sleep(2)

# Now you're logged in and have handled the popups. You can proceed to interact with Instagram further.

# Optionally, you can add more actions like visiting a profile or scrolling through the feed
# For example:
# driver.get("https://www.instagram.com/explore/")

# Remember to close the driver after finishing the automation
# driver.quit()
