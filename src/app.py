#!/usr/bin/env python

from time import sleep
from selenium import webdriver

__author__ = 'khalilj'
__creation_date__ = '04/18/2019'

CHROME_DRIVER_PATH = './web_drivers/chromedriver'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

try:
    driver.get('https://www.google.com')
    sleep(5)
finally:
    driver.quit()
