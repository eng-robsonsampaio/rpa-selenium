
from time import sleep, time
from credentials import login_dte

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

import pyautogui

# Begin
start_time = time()

options = webdriver.ChromeOptions()
options.add_extension(r'.\extensions\Web-PKI.crx')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(r'.\drivers\chromedriver.exe', options=options)
driver.get(login_dte.URL)
driver.maximize_window()

p = driver.current_window_handle
print(f'Windows title:  {driver.title}')
print(f'Windows habdke:  {p}')

sleep(2)
try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@routerlink='/certificado']"))
        )
finally:
    driver.find_element(By.XPATH, "//a[@routerlink='/certificado']").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button")))
finally:
#     sleep(2)
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-certificado/div/ul/li[2]/button").click()
    sleep(3)
    pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[2]/table/tbody/tr[1]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-e-cnpj/div/div[3]/button[2]").click()
    sleep(3)
    pyautogui.hotkey('tab', 'tab', 'enter', interval=0.1)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]").click()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li/a/div").click()


    sleep(5)
    pyautogui.hotkey('enter')
    sleep(5)
    pyautogui.hotkey('enter')
    driver.switch_to.window(driver.window_handles[-1])
    # get current window handle
    sleep(1)
    p = driver.current_window_handle
    print(f'Windows title:  {driver.title}')
    print(f'Windows habdke:  {p}')
    siget_url = driver.current_url
    print(f'\n\nURL{siget_url}\n\n')

try:
    elem = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, 'menu_indicadores_nfe'))
    )
    print(elem)
finally:
    sleep(3)
    driver.find_element(By.ID, "menu_indicadores_nfe").click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[1]/button').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/button').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[2]/div/ul/li[2]/a').click()

# try:    
#     sleep(3)
#     driver.find_element(By.XPATH, '/html/body/app-root/div/app-nfe/div/div/section[2]/div/div/div/div/app-nfe-entradas/div[1]/div[2]/div[1]/button')
#     print(len(elementos))
# finally:
#     pass
    # for el in elementos:
    #     print('Elemento: ', el)
    # driver.find_element(By.XPATH, '//button[@id="tab_entradas"]').click()


#     # sleep(3)
#     # driver.find_element(By.CLASS_NAME, "btn bg-default btn-sm dropdown-toggle").click()

  
print(f'---- {(time() - start_time)} seconds ----')