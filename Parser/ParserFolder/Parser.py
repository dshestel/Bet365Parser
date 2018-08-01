import time
from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver1.exe')

driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')

while 1:
    time.sleep(5)
    count = 0
    elements = driver.find_elements_by_xpath("//div[@class='ipo-ViewSelectorContainer ipo-ViewSelectorContainer_Cid-1 "
                                             "ipo-ViewSelectorContainer_MatchLive ']")
    try:
        stats = driver.find_element_by_xpath("//div[@class='ml1-AllStats ml1-AllStats_PosBar ']")
        print(stats.text)
    except:
        print(len(elements))

    for element in elements:
        elements[count].click()
        count += 1
        time.sleep(2)
        try:
            stats = driver.find_element_by_xpath("//div[@class='ml1-AllStats ml1-AllStats_PosBar ']")
            print(stats.text)
        except:
            print("error")
        time.sleep(2)
        if count == len(elements):
            elements = driver.find_elements_by_xpath(
                "//div[@class='ipo-ViewSelectorContainer ipo-ViewSelectorContainer_Cid-1 "
                "ipo-ViewSelectorContainer_MatchLive ']")
            elements[0].click()
            break
