import time
import os.path
from selenium import webdriver

driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

time.sleep(10)
bar_item = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
for element in bar_item:
    if element.text == "Event View":
        element.click();
        break
time.sleep(10)

# xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div"
#                                       "[3]/div[2]/div/div/div/div[@class='ipn-FixtureButton ']")
#
# time = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]'
#                                     '/div/div/div/div[1]/div[1]/div[2]/div[1]')
#

# closed_element = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]"
#                                                "/div[1]/div/div/div/div[3]/div[2]"
#                                                "/div[@class='ipn-Competition ipn-Competition-closed ']")
#
# for element in closed_element:
#     element.click()
#     time.sleep(2)

#   /html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div[7]/div[2]
#   /html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]/div[5]/div[2]
#
#

try:
    league = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]')
    print(league.text)
except:
    a = 1


# try:
#     markets = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div[3]')
#     print(markets.text)
#
#     split = markets.text.split('\n')
#     full_time_result = []
#     double_chance = []
#     half_time_result = []
#     match_goals = []
#     asian_handicap = []
#
#
#     for i in range(len(split)):
#         if split[i] == 'Fulltime Result':
#             full_time_result.append([split[i+2], split[i+4], split[i+6]])
#             print(full_time_result)
#         if split[i] == 'Double Chance':
#             double_chance.append([split[i+2], split[i+4], split[i+6]])
#             print(double_chance)
#         if split[i] == 'Half Time Result':
#             half_time_result.append([split[i+2], split[i+4], split[i+6]])
#             print(half_time_result)
#         if split[i] == 'Match Goals':
#             match_goals.append([split[i+1], split[i+3], split[i+5]])
#             print(match_goals)
#         if split[i].startswith('Asian Handicap'):
#             asian_handicap.append([[split[i+2], split[i+3]], [split[i+13], split[i+14]]])
#             asian_handicap.append([[split[i+4], split[i+5]], [split[i+15], split[i+16]]])
#             asian_handicap.append([[split[i+6], split[i+7]], [split[i+17], split[i+18]]])
#             asian_handicap.append([[split[i+8], split[i+9]], [split[i+19], split[i+20]]])
#             asian_handicap.append([[split[i+10], split[i+11]], [split[i+21], split[i+22]]])
#             print(asian_handicap)
#         # if split[i].startswith('1st Half Asian Handicap'):
#         #     print(10)
#         #
#         #
#         # if split[i] == 'Goal Line (0-0)':
#         #     print(9)
#         # if split[i] == '1st Half Goal Line (0-0)':
#         #     print(11)
#
# # goal_line = ''
# #     first_half_asian_handicap = ''
# #     first_half_goal_line = ''
#
# except:
#     a = 1