from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/select/single_select')
select_language = driver.find_element(By.ID, 'id_choose_language')
select_language.click()
languages = driver.find_elements(By.TAG_NAME, 'option')
languages[1].click()
submit_form = driver.find_element(By.ID, 'submit-id-submit')
submit_form.click()
result_text = driver.find_element(By.ID, 'result-text')
assert result_text.text == 'Python'
