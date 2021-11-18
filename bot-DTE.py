
from time import sleep, time

from selenium.webdriver.common import alert
from credentials import login_dte
from constants.const import DOWNLOAD_PATH, DRIVER_PATH, WEB_PKI_PATH

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def click_on_element(method, path, wait_time=30):
    try:
        elem = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((method, path)))
        elem.click()
    except:
        print(f'Can not click on {path}')
    
def click_on_alert(driver, wait_time=30):
    try:
        WebDriverWait(driver, wait_time).until(EC.alert_is_present())
        alerta = driver.switch_to.alert
        alerta.accept()
    except:
        print(f'Can not click on alert')
    

sleep(2)
click_on_element(By.XPATH, "//a[@routerlink='/certificado']")

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button")

sleep(3)
pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)
click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]")
   
click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]")


sleep(3)
pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]")

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]")

click_on_element(By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div")

sleep(1)
print(f'Número de janelas: {len(driver.window_handles)}')
driver.switch_to.window(driver.window_handles[-1])

click_on_alert(driver)

click_on_alert(driver)

sleep(2)
p = driver.current_window_handle
print(f'Windows title:  {driver.title}')
print(f'Windows habdke:  {p}')
siget_url = driver.current_url
print(f'\n\nURL{siget_url}\n\n')

click_on_element(By.ID, 'menu_indicadores_nfe')
print('Menu indicadores NFe')
click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[1]/button')
print('Pesquisar')
click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/button')
print('Download')
click_on_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/ul/li[2]/a')
print('Download CSV')
  
print(f'---- {(time() - start_time)} seconds ----')