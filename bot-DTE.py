from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from credentials import login_dte

browser = webdriver.Chrome(r'.\drivers\chromedriver.exe')
browser.get(login_dte.URL)
try:
    elem = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(By.XPATH , "//a[@routerlink='/certificado']"))
finally:
    sleep(1)
    browser.find_element_by_xpath("//a[@routerlink='/certificado']").click()
# print(len(elements))

# element_cnpj = browser.find_element_by_id('login')
# element_cnpj.send_keys(login.CNPJ)

# element_senha = browser.find_element_by_id('senha')
# element_senha.send_keys(login.PSK)

# browser.find_element_by_xpath("//button[@name='entrar']").click()

input('')