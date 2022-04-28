# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:44:52 2022

@author: joaop
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_path = None
search_dir = None

# browser = webdriver.Chrome(executable_path=os.path.join(base_path_c, 'drivers/chromedriver4.exe'))
# new try
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("enable-automation")
chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument("ignore-certificate-errors")

browser = webdriver.Chrome()
cards_casas = browser.find_elements_by_xpath('//div[@data-test-id="property-card"]')



for casa in cards_casas:
    precos = casa.find_elements_by_xpath('.//span[contains(text(),"R$")]')

    print(len(precos))
    for preco in precos:
        print(preco.text)

    preco_atual = precos[-1]
print("peguei", len(cards_casas), " casinhas")

# def find_element_by_xpath(browser, xpath, wait_time=1):
#     try:
#         elemento = WebDriverWait(browser, wait_time).until(
#             EC.presence_of_element_located((By.XPATH, xpath)))
#         return elemento
#     except TimeoutException:
#         print("timeout ", xpath)
#         raise TimeoutException