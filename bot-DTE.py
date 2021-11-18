
from time import sleep, time

from selenium.webdriver.common import alert
from credentials import login_dte
from constants.const import DOWNLOAD_PATH, DRIVER_PATH, WEB_PKI_PATH

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

import pyautogui

# Begin
start_time = time()

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : DOWNLOAD_PATH}
options.add_experimental_option('prefs', prefs)
options.add_extension(WEB_PKI_PATH)
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get(login_dte.URL)
driver.maximize_window()

p = driver.current_window_handle
print(f'Windows title:  {driver.title}')
print(f'Windows habdke:  {p}')


def click_on_element(method, path):
    try:
        elem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((method, path)))
        elem.click()
    except:
        print(f'Can not click on {path}')
    

sleep(2)
click_on_element(By.XPATH, "//a[@routerlink='/certificado']")
# elem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/certificado']")))
# elem.click()
click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button")
# elem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button")))
# elem.click()
sleep(3)
pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)
click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]")
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]"))
#     )
# elem.click()    
click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]")

# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]"))
#     )
# elem.click()
sleep(3)
pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]")
# elem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]")))
# elem.click()

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]")
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]"))
#     )
# elem.click()

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div")
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div"))
#     )
    
# elem.click()
sleep(1)
print(f'Número de janelas: {len(driver.window_handles)}')
driver.switch_to.window(driver.window_handles[-1])

WebDriverWait(driver, 5).until(EC.alert_is_present())
alerta = driver.switch_to.alert
alerta.accept()

WebDriverWait(driver, 5).until(EC.alert_is_present())
alerta = driver.switch_to.alert
alerta.accept()
# get current window handle
sleep(2)
p = driver.current_window_handle
print(f'Windows title:  {driver.title}')
print(f'Windows habdke:  {p}')
siget_url = driver.current_url
print(f'\n\nURL{siget_url}\n\n')

click_on_element(By.ID, 'menu_indicadores_nfe')
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.ID, 'menu_indicadores_nfe'))
#     )   
print('Menu indicadores NFe')
# elem.click()

click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[1]/button')
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[1]/button'))
#     )
print('Pesquisar')
# elem.click()
click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/button')
# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/button'))
#     )
print('Download')
# elem.click()    
click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/ul/li[2]/a')

# elem = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/ul/li[2]/a'))
#     )
print('Download CSV')
# elem.click()
  
print(f'---- {(time() - start_time)} seconds ----')