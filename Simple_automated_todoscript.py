from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chromeservices
from webdriver_manager.chrome import ChromeDriverManager

# init driver
driver = webdriver.Chrome(service=Chromeservices(ChromeDriverManager().install()))
driver.implicitly_wait(5)

# Open URL
driver.get('http://localhost:3000/')


# Create Task on the app
driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Do the laundry")

# Adds the task to the list
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Mark the task as done
driver.find_element(By.XPATH,"//span[@class='icon']").click()

# uncheck the added task
driver.find_element(By.XPATH,'(//ul[@class="Todo-group"]/li/span[text()="[X]"])[3]').click()

# Delete the task
driver.find_element(By.XPATH,"//button[@type='button']").click()



print("5 Test Case Passed")