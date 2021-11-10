
from time import sleep
from credentials import login_dte

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import pyautogui



options = webdriver.ChromeOptions()
options.add_extension(r'.\extensions\Web-PKI.crx')

driver = webdriver.Chrome(r'.\drivers\chromedriver.exe', options=options)
driver.get(login_dte.URL)
try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(By.XPATH , "//a[@routerlink='/certificado']"))
finally:
    sleep(1)
    driver.find_element_by_xpath("//a[@routerlink='/certificado']").click()
    sleep(3)
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button").click()
    sleep(5)
    pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)
    

# input('')