import csv
import time
import os.path
from selenium import webdriver

driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

csvData = [["Time"], ["Attacks"], ["Dangerous Attacks"], ["Possession %"], ["On Target"], ["Off Target"], ["League"], ["Command Name"], ["Score"],
          ["1x2 First command"], ["1x2 The second command"], ["1x2 Draw"], ["Next goal First command"], ["Next goal second command"], ["Next goal Draw"],
          ["Match goals First command"], ["Match goals The second command"], ["Match goals Draw"]]

time.sleep(10)
bar_item = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
for element in bar_item:
    if element.text == "Event View":
        element.click()
        break
time.sleep(5)


while True:
    # for open all closed matches
    closed_element = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]"
                                                   "/div[1]/div/div/div/div[3]/div[2]"
                                                   "/div[@class='ipn-Competition ipn-Competition-closed ']")
    if len(closed_element) > 0:
        for element in closed_element:
            element.click()
            time.sleep(1)

    # best selector
    xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div"
                                          "[3]/div[2]/div/div/div/div[@class='ipn-FixtureButton ']")
    if len(xpath) > 0:
        for element in xpath:
            element.click()
            time.sleep(3)
            data = [[]]
            try:
                time = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                    '/div/div/div/div[1]/div[1]/div[2]/div[1]')
                data = [[time.text]]
            except:
                print("Time error")
                data = [['00:00']]

            try:
                corner = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                      '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[3]')
                split_corner = corner.text.split('\n')
                data.append([split_corner[0], split_corner[1]])
                # print(corner.text)
            except:
                print("Corner error")
                data.append(["None"])

            try:
                yellow_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                           '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[4]')
                split_yellow_card = yellow_card.text.split('\n')
                data.append([split_yellow_card[0], split_yellow_card[1]])
                # print(yellow_card.text)
            except:
                print("yellow_card error")
                data.append(["None"])

            try:
                red_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                        '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[5]')
                split_red_card = red_card.text.split('\n')
                data.append([split_red_card[0], split_red_card[1]])
                # print(red_card.text)
            except:
                print("red_card error")
                data.append(["None"])

            try:
                penalty = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                       '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[9]')
                split_penalty = penalty.text.split('\n')
                data.append([split_penalty[0], split_penalty[1]])
                # print(penalty.text)
            except:
                print("penalty error")
                data.append(["None"])

            try:
                goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                    '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[10]')
                split_goal = goal.text.split('\n')
                data.append([split_goal[0], split_goal[1]])
                # print(goal.text)
            except:
                print("goal error")

            try:
                left_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                            '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]'
                                                            '/div/div[1]')

                right_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                             '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]'
                                                             '/div/div[3]')

                data.append([left_attacks.text, right_attacks.text])
                # print(attacks.text)
            except:
                print("attacks error")
                data.append(["None"])

            try:
                danger_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                              '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]')
                #danger_attacks =
                # print(danger_attacks.text)
            except:
                print("danger_attacks error")
                data.append(["None"])

            try:
                possession = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                          '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[3]')
                # print(possession.text)
            except:
                print("possession error")
                data.append(["None"])

            try:
                on_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                         '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[1]/div')
                # print(on_target.text)
            except:
                print("on_target error")
                data.append(["None"])

            try:
                off_target = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                          '/div/div/div/div[3]/div/div/div/div[3]/div[4]/div[2]/div')
                # print(off_target.text)
            except:
                print("off_target error")
                data.append(["None"])

            try:
                full_time_result = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                                '/div[2]/div/div/div/div[3]/div[2]/div[2]')
                # print(full_time_result.text)
            except:
                print("full_time_result error")
                data.append(["None"])

            try:
                double_chance = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                             '/div[2]/div/div/div/div[3]/div[3]/div[2]')
                # print(double_chance.text)
            except:
                print("double_chance error")
                data.append(["None"])

            try:
                half_time_result = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                                '/div[2]/div/div/div/div[3]/div[4]/div[2]/div')
                # print(half_time_result.text)
            except:
                print("half_time_result error")
                data.append(["None"])

            try:
                first_goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                          '/div[2]/div/div/div/div[3]/div[5]/div[2]/div')
                # print(first_goal.text)
            except:
                print("first_goal error")
                data.append(["None"])

            try:
                match_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                           '/div[2]/div/div/div/div[3]/div[6]/div[2]/div')
                # print(match_goals.text)
            except:
                print("match_goals error")
                data.append(["None"])

            try:
                alternative_match_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div'
                                                                       '/div[2]/div[2]/div/div/div/div[3]/div[7]'
                                                                       '/div[2]/div')
                # print(alternative_match_goals.text)
            except:
                print("alternative_match_goals error")
                data.append(["None"])

            try:
                first_half_goals = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                                '/div[2]/div/div/div/div[3]/div[8]/div[2]/div')
                # print(first_half_goals.text)
            except:
                print("first_half_goals error")
                data.append(["None"])

            try:
                asian_handicap = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                              '/div[2]/div/div/div/div[3]/div[9]/div[2]/div')
                print(asian_handicap.text)
            except:
                print("asian_handicap error")
                data.append(["None"])

            try:
                goal_line = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                         '/div[2]/div/div/div/div[3]/div[10]/div[2]/div')
                # print(goal_line.text)
            except:
                print("goal_line error")
                data.append(["None"])

    else:
        print("else")
    # break