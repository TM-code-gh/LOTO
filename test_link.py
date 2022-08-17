# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:53:04 2022

@author: theom
"""
import os.path
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

start = time.time()

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe',options=option)

driver.get('https://www.fdj.fr/jeux-de-tirage/loto/resultats')

#count=driver.find_element_by_xpath('//*[@id="page-chart"]/section[3]/div/div/section[1]/div')

parentElement = driver.find_elements_by_class_name('history-result_content')[0]
elementList = parentElement.find_elements_by_class_name('history-result_content-item')

child = len(elementList)


print(child)

driver.quit()

end = time.time()
print(end - start)