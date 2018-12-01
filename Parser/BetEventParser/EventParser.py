import time
import os.path
from selenium import webdriver
import sys

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

# best selector
xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div"
                                      "[3]/div[2]/div/div/div/div[@class='ipn-FixtureButton ']")

for element in xpath:
    element.click()
    time.sleep(3)
    try:
        corner = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                              '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[3]')
        # print(corner.text)
    except:
        print("Corner error")

    try:
        yellow_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                   '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[4]')
        # print(yellow_card.text)
    except:
        print("yellow_card error")

    try:
        red_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[5]')
        # print(red_card.text)
    except:
        print("red_card error")

    try:
        penalty = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                               '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[9]')
        # print(penalty.text)
    except:
        print("penalty error")

    try:
        goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                            '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[10]')
        # print(goal.text)
    except:
        print("goal error")

    try:
        attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                               '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div')
        # print(attacks.text)
    except:
        print("attacks error")

    try:
        danger_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                      '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]')
        # print(danger_attacks.text)
    except:
        print("danger_attacks error")

    try:
        possession = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                  '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[3]')
        # print(possession.text)
    except:
        print("possession error")

    try:
        on_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                 '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[1]/div')
        # print(on_target.text)
    except:
        print("on_target error")

    try:
        off_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                  '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[2]/div')
        # print(off_target.text)
    except:
        print("off_target error")

    try:
        full_time_result = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                        '/div[2]/div/div/div/div[3]/div[2]/div[2]')
        # print(full_time_result.text)
    except:
        print("full_time_result error")

    try:
        double_chance = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                     '/div[2]/div/div/div/div[3]/div[3]/div[2]')
        # print(double_chance.text)
    except:
        print("double_chance error")

    try:
        half_time_result = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                        '/div[2]/div/div/div/div[3]/div[4]/div[2]/div')
        # print(half_time_result.text)
    except:
        print("half_time_result error")

    try:
        first_goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                  '/div[2]/div/div/div/div[3]/div[5]/div[2]/div')
        # print(first_goal.text)
    except:
        print("first_goal error")

    try:
        match_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                   '/div[2]/div/div/div/div[3]/div[6]/div[2]/div')
        # print(match_goals.text)
    except:
        print("match_goals error")

    try:
        alternative_match_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                               '/div[2]/div/div/div/div[3]/div[7]/div[2]/div')
        # print(alternative_match_goals.text)
    except:
        print("alternative_match_goals error")

    try:
        first_half_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                        '/div[2]/div/div/div/div[3]/div[8]/div[2]/div')
        # print(first_half_goals.text)
    except:
        print("first_half_goals error")

    try:
        asian_handicap = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                      '/div[2]/div/div/div/div[3]/div[9]/div[2]/div')
        print(asian_handicap.text)
    except:
        print("asian_handicap error")

    try:
        goal_line = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                 '/div[2]/div/div/div/div[3]/div[10]/div[2]/div')
        # print(goal_line.text)
    except:
        print("goal_line error")

    # break

# print(len(xpath))
#
# for element in xpath:
#     element.click()
#     time.sleep(2)
