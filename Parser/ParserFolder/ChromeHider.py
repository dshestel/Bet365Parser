from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
#options.add_argument('--headless')
#options.add_argument('--enable-gpu-benchmarking')
#options.headless = true
#options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe', chrome_options=options)
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
time.sleep(5)
count = 0
elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")
#driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')


time.sleep(4)
print(len(elements))


driver.quit()