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
base_url = 'https://www.primark.com/en-gb/stores?country=united-kingdom&lat=54.7877149&lng=-6.4923145&storeQuery=northern+ireland&zoom=9'
driver.get(base_url)

# import urllib2
print('path: ', os.getcwd())

cookie_clicker = 0
stores_list = []
centre_list = []
address_list = []
stores_dict = {
    'Address': "",
    'Centre Name': "",
    'Store Name': "Primark"
}

#cookie_clicker = 0
#driver.find_element(By.XPATH, '//*[@id="yext"]/article/div/div[2]/form/button').click()
#xpath_query = "/html/body/div[4]/div[3]/*"
#xpath_query = '//html//body//div[1]//div[2]//div//div[1]//div[4]//div[2]//p[1]' 
xpath_query = '//html//body//div[1]//div[2]//div//div[1]//div[4]//div[@data-store-id]'
# 10.1 mi 
# 30 A Tower Centre, Wellington Street, Ballymena
#xpath_query = '//html//body//div[1]//div[2]//div//div[1]//div[4]//div[2]' 
# Ballymena10.1 mi30 A Tower Centre, Wellington Street, BallymenaOpen until 17:30Store details
results = driver.find_elements(By.XPATH, '//h5')
results2 = driver.find_elements(By.XPATH, xpath_query)
#results2 = driver.find_elements(By.XPATH, "//span//p[contains(@class, 'MuiTypography-root jss157 MuiTypography-body1')]") worked
#results = driver.find_elements(By.TAG_NAME, "stores-list") didnt work
#results = driver.find_elements(By.CLASS_NAME, "MuiBox-root jss139 jss128 jss137") didnt work
#results = driver.find_elements(By.ID, "456") didnt work

#print("-----Attempting to print results-----")
#print(results)
#print(results2)



if cookie_clicker == 0:
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        cookie_clicker += 1
        time.sleep(3)

print("-----looping-----")
#for each store found, add to list
for result in results2:
    #print (result.text)
    #print (result.get_attribute("title"))
    #for strong_tag in soup.find_all('strong'):
    #    print(strong_tag.text)
    #    stores_list.append(strong_tag.text)
    #print (soup.prettify())
    
    driver.find_element(By.LINK_TEXT, 'Store details').click()
    print('we clicked')
    time.sleep(5)
    results3 = driver.find_element(By.XPATH, "//html//body//div[1]//div[2]//div[1]//div[1]//div//div[2]//div//div//div[2]")
    print(results3.text)
    time.sleep(3)
    driver.back()
    time.sleep(3)
    try:
        #webdriver.find_element(By.XPATH('//*[@id="evg-exit-intent-popup-email-capture"]/div/button'))
        driver.find_element(By.XPATH,'//*[@id="evg-exit-intent-popup-email-capture"]/div/button').click()
        print ("popup found")
        break
    except Exception:
         print ("no popup this time")
         break
    #soup = BeautifulSoup(''.join(results3.get_attribute("data-store-id")))
    #print ((result.get_attribute("innerHTML")))
    #centre_list.append(soup.text)
    #print (type(result.get_attribute("innerHTML")))
    time.sleep(3)

#driver.find_element(By.LINK_TEXT, 'Store details').click()
#time.sleep(20)

#take the postcode
#return to base url/take page

# for result in results2:
#     #print (result.text)
#     #print (result.get_attribute("title"))
#     soup = BeautifulSoup(''.join(result.get_attribute("innerHTML")))
#     #for strong_tag in soup.find_all('strong'):
#     #    print(strong_tag.text)
#     #    stores_list.append(strong_tag.text)
#     #print (soup.prettify())
#     print (soup.text)
#     #print ((result.get_attribute("innerHTML")))
#     address_list.append(soup.text)
#     #print (type(result.get_attribute("innerHTML")))
#     time.sleep(5)

#When scraping centres for stores within
#stores_dict['Store Name'] = stores_list
#stores_df = pd.DataFrame(stores_dict)

#When scraping stores in multiple centres
stores_dict['Centre Name'] = centre_list
stores_dict['Address'] = address_list
#stores_df = pd.DataFrame(stores_dict) 

print("--------")
#print(stores_df)


#stores_df.to_csv('C:/Users/Jack/Desktop/Scrapes/primark_NI.csv')

