from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
  
driver = webdriver.Chrome()
driver.get("https://www.cermati.com/gabung")
driver.maximize_window()

try:
  element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "email"))
  )
finally:
  driver.find_element_by_name("email").send_keys("oktaviansyah47@yahoo.com")
  driver.find_element_by_name("password").send_keys("yourpassword1")
  driver.find_element_by_name("confirmPassword").send_keys("yourpassword1")
  driver.find_element_by_name("firstName").send_keys("Okta")
  driver.find_element_by_name("lastName").send_keys("Viansyah")
  driver.find_element_by_name("mobilePhone").send_keys("085157972253")
  city = driver.find_element_by_name("residenceCity")
  city.send_keys("Bogor")
  try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "autocomplete-list-item"))
    )
  finally:
    city.send_keys(Keys.ARROW_DOWN)
    city.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//button[@type='submit']").click()
