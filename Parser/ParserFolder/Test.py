# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('D:/chromedriver1.exe')
#
# #driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')
# driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
# driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
#
# #<div class="ipo-Classification sport_1 "><h4 class="ipo-Classification_Name">Soccer</h4></div>
# while 1:
#     time.sleep(5)
#     elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")
#     if len(elements) == 0:
#         # <div class="ip-ControlBar_BBarItem " style="">Overview</div>
#         elements1 = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
#         print(elements1[0].text)
#         #if len(elements1) > 0:
#         #    elements1[0].click()


import time
import os.path
from selenium import webdriver


driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

time.sleep(5)
bar_item = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
for element in bar_item:
    if element.text == "Event View":
        element.click();
        break
time.sleep(10)

#useless
#elements = driver.find_elements_by_xpath("//div[@class='ipn-ClassificationContainer ']")
#my = driver.find_elements_by_xpath("//div[@class='ipn-Competition ']")
#sockerMatches = driver.find_elements_by_xpath("//div[@class='ipn-Fixture ipn-Fixture_HasTeamStack ipn-Fixture-closed ipn-Fixture-hastimer ']")
#sockerMatches1 = driver.find_elements_by_xpath("//div[@class='ipn-ClassificationButton ipn-ClassificationButton_Classification-1 ']")
#useless

#best option
opening = driver.find_elements_by_xpath("//div[@class='ipn-Classification ipn-Classification-open ']")
#best option

#try
xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div")
#

print(len(xpath))
for element in xpath:
    print(element.text)
#print(len(opening))
#print(opening[0].text)

# s = elements[0].text.split("\n")
# print(len(s))
# print(len(my))
# print(len(sockerMatches))
# for element in sockerMatches:
#     print(element.text)