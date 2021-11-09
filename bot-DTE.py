
from time import sleep
from credentials import login_dte

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_extension(r'.\extensions\Web-PKI.crx')

browser = webdriver.Chrome(r'.\drivers\chromedriver.exe', options=options)
browser.get(login_dte.URL)
try:
    elem = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(By.XPATH , "//a[@routerlink='/certificado']"))
finally:
    sleep(1)
    browser.find_element_by_xpath("//a[@routerlink='/certificado']").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button").click()
    sleep(3)
    alert = browser.switch_to_alert()

input('')