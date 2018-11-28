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
time.sleep(5)


#xpath for match in league
#/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div[1]/div[4]/div/div[1]
#/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]/div[4]/div[2]
#/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]/div[4]
#/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div


#best selesction
xpath = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div/div/div[@class='ipn-FixtureButton ']")

print(len(xpath))

for element in xpath:
    element.click()
    time.sleep(2)