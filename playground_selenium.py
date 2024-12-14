import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

USERNAME_FIELD = "sales.admjabsel@dgw.co.id"
PASSWORD_FIELD = "010195"
DATE_FROM = "14/10/2024"
DATE_TO = "14/11/2024"

# Set up the WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Open a web page
driver.get("https://spartan.dgw.co.id/login/")

# Locate the email field using XPath
username_field = driver.find_element(
    "xpath", "/html/body/div/div[2]/div[2]/div/form/div[3]/div/div[1]/div/div/input"
)
password_field = driver.find_element(
    "xpath", "/html/body/div/div[2]/div[2]/div/form/div[3]/div/div[2]/div/div/input"
)
login_button = driver.find_element(
    "xpath", "/html/body/div/div[2]/div[2]/div/form/div[4]/button"
)

# Enter your login credentials
username_field.send_keys(USERNAME_FIELD)
password_field.send_keys(PASSWORD_FIELD)

# Click the login button
login_button.click()

# Click the inbox button
inbox_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/div/div/ul/span[3]/li/div")
    )
)
inbox_button.click()

# Click 'Sudah Diproses' button
sudah_diproses_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div/div[2]/main/div[2]/div[1]/div[2]/div/div/div/button[2]",
        )
    )
)
sudah_diproses_button.click()


# Click filter button
filter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div[1]")
    )
)
filter_button.click()

from_date_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/input")
    )
)
driver.execute_script("arguments[0].removeAttribute('readonly')", from_date_field)
from_date_field.clear()
from_date_field.send_keys(DATE_FROM)

# Locate and manipulate the to_date_field
to_date_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/input")
    )
)
driver.execute_script("arguments[0].removeAttribute('readonly')", to_date_field)
to_date_field.clear()
to_date_field.send_keys(DATE_TO)

# Click the select field
select_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[4]/div/div/div")
    )
)
select_field.click()

# Choose an option from the dropdown
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div[3]/ul/li[4]")
    )
)
option.click()

# Click the final button
final_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div[5]/div[3]/button")
    )
)
final_button.click()

# Wait for the results to load
results_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[5]/div/div/ul")
    )
)

# Wait for the child `li` elements to be present
child_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[5]/div/div/ul/li")
    )
)
print(f"Number of child elements: {len(child_elements)}")

# Initialize a list to store the data
data = []

# Click each `li` element and copy the content
for i in range(len(child_elements)):
    try:
        # Re-locate the `li` elements to avoid stale element reference
        child_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div[5]/div/div/ul/li")
            )
        )
        child_elements[i].click()
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/main/div[2]/div[2]/div[4]/div[2]/div/div/div/div/div/div/div/table")
            )
        )
        table_html = table.get_attribute('outerHTML')
        data.append(table_html)
    except StaleElementReferenceException:
        print(f"StaleElementReferenceException encountered for element {i}")

# Save the data into a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Just for not let the browser immediate closed
time.sleep(2)

# Remove the code that closes the browser
driver.quit()
