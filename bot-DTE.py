
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
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(r'.\drivers\chromedriver.exe', options=options)
driver.get(login_dte.URL)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/certificado']")))
finally:
    # driver.find_elements_by_partial_link_text('#/Certificado').click()
    driver.find_element_by_xpath("//a[@routerlink='/certificado']").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button")))
finally:
#     sleep(2)
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button").click()
    sleep(3)
    pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]"))
    )
finally:
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]"))
    )
finally:
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]").click()
    sleep(5)
    pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]"))
    )
finally:
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]"))
    )
finally:
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div"))
    )
finally:
    driver.find_element_by_xpath("/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div").click()
    sleep(5)
    pyautogui.hotkey('enter')
    sleep(5)
    pyautogui.hotkey('enter')
# WebDriverWait(driver, 30).until(EC.alert_is_present())
# print('Alert is on')
# alert = driver.switch_to_alert
# sleep(1)
# pyautogui.hotkey('enter')
# sleep(1)
# WebDriverWait(driver, 30).until(EC.alert_is_present())
# print('Alert is on')
# alert = driver.switch_to_alert
# sleep(1)
# pyautogui.hotkey('enter')
    
    # sleep(1)
    # alert = WebDriverWait(driver, 30).until(EC.alert_is_present())
    # sleep(0.5)
    # print('Alert is on')
    # pyautogui.hotkey('enter')

# try:
#     elem = WebDriverWait(driver, 30).until(EC.alert_is_present())
# finally:
#     pyautogui.hotkey('enter')

# try:
#     elem = WebDriverWait(driver, 30).until(EC.alert_is_present())
# finally:
#     pyautogui.hotkey('enter')


#     pyautogui.hotkey('enter')
#     sleep(5)
#     pyautogui.hotkey('enter')

    # /html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div
# input('')