#import requests
#import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import json
import os
import time

chrome_options = Options()
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_options.add_experimental_option("deatch",True)
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

#driver = webdriver.Chrome(executable_path=r'C:\\vscode\\webdriver\\chromedriver')
options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Base url
base_url = 'https://www.thejunctionshopping.com/stores/'
driver.get(base_url)

# import urllib2
print('path: ', os.getcwd())


stores_list = []
coords_list = []
stores_dict = {
    'Centre Name': "Antrim - The Junction",
    'Store Name': ""
}

#cookie_clicker = 0
#driver.find_element(By.XPATH, '//*[@id="yext"]/article/div/div[2]/form/button').click()
#xpath_query = "/html/body/div[4]/div[3]/*"
xpath_query = '//p[contains(., "title")]//a'
results = driver.find_elements(By.CLASS_NAME, "title")
#print(results)

for result in results:
    #print (result.text)
    #print (result.get_attribute("title"))
    soup = BeautifulSoup(''.join(result.get_attribute("innerHTML")))
    #for strong_tag in soup.find_all('strong'):
    #    print(strong_tag.text)
    #    stores_list.append(strong_tag.text)
    #print (soup.prettify())
    print (soup.text)
    #print ((result.get_attribute("innerHTML")))
    stores_list.append(soup.text)
    #print (type(result.get_attribute("innerHTML")))
    time.sleep(5)

# time.sleep(5)
# print(driver.find_element(By.XPATH, xpath_query).get_attribute("innterHTML"))
# time.sleep(5)

# c = driver.find_element(By.XPATH, "//html/body/div[4]/div[3]")
#     # c = driver.find_element(By.CSS_SELECTOR,'#schema-location > script')
# c = c.get_attribute("innerHTML")
# print('THIS IS C', c)
# c = json.loads(c)
# time.sleep(3)

stores_dict['Store Name'] = stores_list
stores_df = pd.DataFrame(stores_dict)

print("--------")
print(stores_df)


stores_df.to_csv('C:/Users/Jack/Desktop/Scrapes/antrim.csv')

