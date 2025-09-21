from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 3)
driver.get('https://demoqa.com/automation-practice-form')
first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('first')
last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('last')
email = driver.find_element(By.ID, 'userEmail')
email.send_keys('test@gmail.com')
gender = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
gender.click()
mobile_number = driver.find_element(By.ID, 'userNumber')
mobile_number.send_keys('1234567890')
birthday = driver.find_element(By.ID, 'dateOfBirthInput')
birthday.click()
months = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-dropdown-container--select')
months.click()
selected_month = driver.find_element(By.CSS_SELECTOR, '[value="4"]')
selected_month.click()
selected_day = driver.find_element(By.CLASS_NAME, 'react-datepicker__day--005')
selected_day.click()
subjects = driver.find_element(By.ID, 'subjectsInput')
subjects.send_keys('ch')
subjects.send_keys(Keys.ENTER)
hobby = driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-1"]')
hobby.click()
adress = driver.find_element(By.ID, 'currentAddress')
adress.send_keys('test')
state = driver.find_element(By.ID, 'state')
driver.execute_script("arguments[0].click();", state)
state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
state_input.send_keys("NCR")
state_input.send_keys(Keys.ENTER)
city_dropdown = driver.find_element(By.ID, "city")
city_dropdown.click()
city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
city_input.send_keys("De")
city_input.send_keys(Keys.ENTER)
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
table = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "table-responsive"))
)
all_data = {}

rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 2:
        key = cells[0].text
        value = cells[1].text
        all_data[key] = value

print("Введенные значения:")
print(all_data)
