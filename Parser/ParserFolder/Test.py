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
#
# print(len(closed_element))

# print(time.text)

left_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                            '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div/div[1]')
right_attacks = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
                                             '/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div/div[3]')


# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div
# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div/div[1]
# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[3]/div[2]/div[1]/div/div[3]
#sp = penalty.text.split('\n')
#print(sp[0] + ":" + sp[1])

print(left_attacks.text)
print(right_attacks.text)


#<div class="ipn-Competition ipn-Competition-closed "><div class="ipn-CompetitionButton " style="">Spain Segunda B</div><div class="ipn-Competition_Icon "></div><div class="ipn-Competition_FavouriteButton "></div></div>
# /html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div[@class='ipn-Competition ipn-Competition-closed ']