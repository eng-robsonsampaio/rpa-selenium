from selenium import webdriver
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

sleep(5)
browser.find_element_by_id('mostrarPendencia').click()
sleep(3)

# browser.find_element_by_xpath('//*[@id="ToolTables_2b81d69e1cd846edcf6f0b482bb82cf8_0"]').click()
# browser.find_element_by_id('ToolTables_adce851614cc2cec446efc69bba3a044_0').click()
browser.find_element_by_xpath('//a[@class="DTTT_button ui-button ui-state-default DTTT_button_text"]').click()
sleep(3)

browser.find_element_by_id('botao_imprimir_map').click()
sleep(3)

# browser.find_element_by_id(id_='empresa').click()
# element.click()

# browser.find_element_by_xpath("//input[@value='empresa']").click()
# element_empresa = browser.find_element_by_id(id_='empresa').click()
# sleep(2)
# element_empresa.click()
# cpf_input.send_keys('02781607355')

input('')