from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# from credentials/login import 
from credentials import login

browser = webdriver.Chrome(r'.\drivers\chromedriver.exe')

browser.get(login.URL)
# sleep(2)
browser.find_element_by_xpath("//label[@for='empresa']").click()

element_cnpj = browser.find_element_by_id('login')
element_cnpj.send_keys(login.CNPJ)

element_senha = browser.find_element_by_id('senha')
element_senha.send_keys(login.PSK)

browser.find_element_by_xpath("//button[@name='entrar']").click()

# sleep(5)
# browser.find_element_by_id('mostrarPendencia').click()
# sleep(3)

# browser.find_element_by_xpath('//a[@class="DTTT_button ui-button ui-state-default DTTT_button_text"]').click()
# sleep(3)

# browser.find_element_by_id('botao_imprimir_map').click()
# sleep(3)

input('')