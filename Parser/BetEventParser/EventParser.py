import time
import os.path
from selenium import webdriver

driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

time.sleep(20)
bar_item = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
for element in bar_item:
    if element.text == "Event View":
        element.click();
        break
time.sleep(5)

# attacks
# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]

# best selector
xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div"
                                      "[3]/div[2]/div/div/div/div[@class='ipn-FixtureButton ']")

for element in xpath:
    element.click()
    time.sleep(3)
    corner = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                          '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[3]')
    yellow_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                               '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[4]')
    red_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                            '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[5]')
    penalty = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                           '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[9]')
    goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                        '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[10]')
    attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                           '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div')
    danger_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                  '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]')
    possession = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                              '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[3]')
    on_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                             '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[1]/div')
    off_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                              '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[2]/div')
    # print(corner.text)
    # print(yellow_card.text)
    # print(red_card.text)
    # print(penalty.text)
    # print(goal.text)
    # print(attacks.text)
    # print(danger_attacks.text)
    # print(possession.text)
    # print(on_target.text)
    # print(off_target.text)
    break

# print(len(xpath))
#
# for element in xpath:
#     element.click()
#     time.sleep(2)
