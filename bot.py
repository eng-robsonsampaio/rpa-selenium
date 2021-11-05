from selenium import webdriver
from time import sleep
# from credentials/login import 

CNPJ = '26.221.703/0001-33'
PSK = 'maikon123'
URL_LOGIN = 'https://servicos-crea-ce.sitac.com.br/'

browser = webdriver.Chrome(r'.\drivers\chromedriver.exe')

browser.get(URL_LOGIN)
# sleep(2)
browser.find_element_by_xpath("//label[@for='empresa']").click()

element_cnpj = browser.find_element_by_id('login')
element_cnpj.send_keys(CNPJ)

element_senha = browser.find_element_by_id('senha')
element_senha.send_keys(PSK)

browser.find_element_by_xpath("//button[@name='entrar']").click()

sleep(5)
browser.find_element_by_id('mostrarPendencia').click()
sleep(3)

# browser.find_element_by_id('ToolTables_7fb7215bf87a89a9394279a77ff70dcb_0').click()
# sleep(3)

# browser.find_element_by_id('botao_imprimir_map').click()
# sleep(3)

# browser.find_element_by_id(id_='empresa').click()
# element.click()

# browser.find_element_by_xpath("//input[@value='empresa']").click()
# element_empresa = browser.find_element_by_id(id_='empresa').click()
# sleep(2)
# element_empresa.click()
# cpf_input.send_keys('02781607355')

input('')