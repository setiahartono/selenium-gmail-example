# RUN CHROME IN DEBUGGING MODE FIRST
# chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Users\ASUS\Documents\Python Projects\raynaldo\data"

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

GMAIL_ACCOUNT = "provideyouremail@examplegmail.com"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver = webdriver.Chrome(options=chrome_options)

# Base function to click after loaded
def click_after_loaded(xpath, url=None):
    element_not_found = True
    if url is not None:
        driver.get(url)
    while element_not_found:
        try:
            element = driver.find_element_by_xpath(xpath)
            element.click()
            element_not_found = False
        except NoSuchElementException:
            time.sleep(1)

# Simple login to Todoist (Example)
url = "https://todoist.com/auth/login"
xpath = "//*[contains(text(), 'Continue with Google')]"
click_after_loaded(xpath, url)

xpath = "//*[contains(text(), '%s')]" % GMAIL_ACCOUNT
click_after_loaded(xpath)
