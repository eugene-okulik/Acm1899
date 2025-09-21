from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
input_data = 'test'
driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = driver.find_element(By.NAME, 'text_string')
text_string.send_keys(input_data)
text_string.send_keys(Keys.ENTER)
result_text = driver.find_element(By.ID, 'result-text')
print(result_text.text)
