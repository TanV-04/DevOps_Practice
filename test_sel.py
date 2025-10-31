from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start a new Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box (by its HTML name attribute)
search_box = driver.find_element(By.NAME, "q")

# Type a search query
search_box.send_keys("What is Selenium?")
search_box.send_keys(Keys.RETURN)

# Wait a bit, then close
driver.quit()
