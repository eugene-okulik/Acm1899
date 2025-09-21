from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
sleep(2)
button = driver.find_element(By.TAG_NAME, 'button')
button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'finish')))
results = driver.find_elements(By.TAG_NAME, 'h4')
assert results[1].text == 'Hello World!'
