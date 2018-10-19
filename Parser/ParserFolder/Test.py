import time
from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver1.exe')

#driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

#<div class="ipo-Classification sport_1 "><h4 class="ipo-Classification_Name">Soccer</h4></div>
while 1:
    time.sleep(5)
    elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")
    if len(elements) == 0:
        # <div class="ip-ControlBar_BBarItem " style="">Overview</div>
        elements1 = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
        print(elements1[0].text)
        #if len(elements1) > 0:
        #    elements1[0].click()