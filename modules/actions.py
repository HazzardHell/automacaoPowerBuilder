from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_window(driver, element_name):
    win = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("name", element_name))
    )
    win.click()
