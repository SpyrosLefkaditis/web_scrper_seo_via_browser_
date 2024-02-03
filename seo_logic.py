from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "your url"

# Set up the browser (make sure you have the appropriate webdriver installed)
driver = webdriver.Chrome()
driver.get(url)

# Find and click the button
button = driver.find_element(By.CSS_SELECTOR, ".button--white")
button.click()

# Add a delay to keep the browser open for 5 seconds (adjust as needed)
time.sleep(20)
