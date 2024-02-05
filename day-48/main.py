from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "D:\CS\Softwares\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("http://www.yahoo.com")
assert 'Yahoo' in driver.title

driver.find_element(By.ID, )
assert 'Yahoo' in driver.title

elem = driver.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN) 

driver.quit()
