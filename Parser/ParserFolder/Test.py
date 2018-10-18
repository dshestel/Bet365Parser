import time
from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver1.exe')

driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')
#<div class="ipo-Classification sport_1 "><h4 class="ipo-Classification_Name">Soccer</h4></div>
while 1:
    time.sleep(5)
    elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")
    if len(elements) == 0:
        elements1 = driver.find_elements_by_xpath("//div[@class='ipo-Classification sport_1 ']")
        print(len(elements1))
        if len(elements1) > 0:
            elements1[0].click()