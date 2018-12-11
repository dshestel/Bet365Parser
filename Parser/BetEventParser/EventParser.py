import csv
import time
import os.path
from selenium import webdriver

driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

csvData = [["League"], ["Command Name"], ["Time"], ["Corner"], ["Yellow Card"], ["Red Card"],
           ["Penalty"], ["Goal"], ["Attacks"], ["Dangerous Attacks"], ["Possession %"],
           ["On Target"], ["Off Target"], ["Fulltime result"], ["Double Chance"], ["Half time result"],
           ["Match Goals"], ["Asian Handicap"]]

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
            try:
                element.click()
                time.sleep(3)

                # tmp data
                data = []
                full_time_result = []
                double_chance = []
                half_time_result = []
                match_goals = []
                asian_handicap = []
                split_league = []
                #
                try:
                    league = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]')
                    split_league = league.text.split('\n')

                    if len(split_league) > 1:
                        data.append([split_league[0]])
                        data.append([split_league[1]])
                    else:
                        data.append(['None'])
                        data.append([split_league[0]])
                except:
                    print("league & command name error")

                try:
                    timer = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                         '/div/div/div/div[1]/div[1]/div[2]/div[1]')
                    data = [[timer.text]]
                except:
                    print("Time error")
                    data = [['00:00']]

                try:
                    corner = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                          '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[3]')
                    split_corner = corner.text.split('\n')
                    data.append([split_corner[0], split_corner[1]])
                except:
                    print("Corner error")
                    data.append(["None"])

                try:
                    yellow_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]'
                                                               '/div[2]/div/div/div/div[1]/div[1]/div[2]/div[3]/div[4]')
                    split_yellow_card = yellow_card.text.split('\n')
                    data.append([split_yellow_card[0], split_yellow_card[1]])
                except:
                    print("yellow_card error")
                    data.append(["None"])

                try:
                    red_card = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                            '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[5]')
                    split_red_card = red_card.text.split('\n')
                    data.append([split_red_card[0], split_red_card[1]])
                except:
                    print("red_card error")
                    data.append(["None"])

                try:
                    penalty = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                           '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[9]')
                    split_penalty = penalty.text.split('\n')
                    data.append([split_penalty[0], split_penalty[1]])
                except:
                    print("penalty error")
                    data.append(["None"])

                try:
                    goal = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
                                                        '/div/div/div/div[1]/div[1]/div[2]/div[3]/div[10]')
                    split_goal = goal.text.split('\n')
                    data.append([split_goal[0], split_goal[1]])
                except:
                    print("goal error")

                try:
                    left_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                                                '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]'
                                                                '/div/div[1]')

                    right_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                 '/div[1]/div/div/div/div[3]/div/div/div/div[3]/div[2]'
                                                                 '/div[1]/div/div[3]')

                    data.append([left_attacks.text, right_attacks.text])
                except:
                    print("attacks error")
                    data.append(["None"])

                try:
                    danger_attacks_left = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                        '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]/div/div[1]')
                    danger_attacks_right = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                        '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[2]/div/div[3]')
                    data.append([danger_attacks_left.text, danger_attacks_right.text])
                except:
                    print("danger_attacks error")
                    data.append(["None"])

                try:
                    possession_left = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                   '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                   '/div[2]/div[3]/div/div[1]')
                    possession_right = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                    '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                    '/div[2]/div[3]/div/div[3]')
                    data.append([possession_left.text, possession_right.text])
                except:
                    print("possession error")
                    data.append(["None"])

                try:
                    on_target_left = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                  '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                  '/div[4]/div[1]/div/span[1]')
                    on_target_right = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                   '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                   '/div[4]/div[1]/div/span[2]')

                    data.append([on_target_left.text, on_target_right.text])
                except:
                    print("on_target error")
                    data.append(["None"])

                try:
                    off_target_left = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                   '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                   '/div[4]/div[2]/div/span[1]')
                    off_target_right = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div'
                                                                    '/div[1]/div/div/div/div[3]/div/div/div/div[3]'
                                                                    '/div[4]/div[2]/div/span[2]')

                    data.append([off_target_left.text, off_target_right.text])
                except:
                    print("off_target error")
                    data.append(["None"])

                try:
                    markets = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]')

                    split = markets.text.split('\n')

                    for i in range(len(split)):
                        if split[i] == 'Fulltime Result':
                            full_time_result.append([split[i + 2], split[i + 4], split[i + 6]])
                        if split[i] == 'Double Chance':
                            double_chance.append([split[i + 2], split[i + 4], split[i + 6]])
                        if split[i] == 'Half Time Result':
                            half_time_result.append([split[i + 2], split[i + 4], split[i + 6]])
                        if split[i] == 'Match Goals':
                            match_goals.append([split[i + 1], split[i + 3], split[i + 5]])
                        if split[i].startswith('Asian Handicap'):
                            asian_handicap.append([[split[i + 2], split[i + 3]], [split[i + 13], split[i + 14]]])
                            asian_handicap.append([[split[i + 4], split[i + 5]], [split[i + 15], split[i + 16]]])
                            asian_handicap.append([[split[i + 6], split[i + 7]], [split[i + 17], split[i + 18]]])
                            asian_handicap.append([[split[i + 8], split[i + 9]], [split[i + 19], split[i + 20]]])
                            asian_handicap.append([[split[i + 10], split[i + 11]], [split[i + 21], split[i + 22]]])
                except:
                    print("Markets error")

                data.append(full_time_result)
                data.append(double_chance)
                data.append(half_time_result)
                data.append(match_goals)
                data.append(asian_handicap)

                if len(split_league) > 1:
                    file_exist = os.path.isfile('D:/NewMatchDataset/' + split_league[0] + ' ' + split_league[1] + '.csv')
                    file = open('D:/NewMatchDataset/' + split_league[0] + ' ' + split_league[1] + '.csv', 'a+', newline='')
                    writer = csv.writer(file)
                else:
                    file_exist = os.path.isfile('D:/NewMatchDataset/' + split_league[0] + '.csv')
                    file = open('D:/NewMatchDataset/' + split_league[1] + '.csv', 'a+', newline='')
                    writer = csv.writer(file)

                if not file_exist:
                    writer.writerow(csvData)

                writer.writerow(data)

            except:
                print("click error")
                break

    else:
        time.sleep(20)
