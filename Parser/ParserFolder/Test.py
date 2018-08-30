test = "1"

print(1 + int(test))


# import csv
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('D:/chromedriver1.exe')
#
# driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')
#
# myData = [["Attacks"], ["Dangerous Attacks"], ["Possession %"], ["On Target"], ["Off Target"], ["Command Name"]]
#
# myFile = open('D:/example11.csv', 'w')
#
# count = 165
#
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerow(myData)
#     while count > 0:
#         time.sleep(30)
#         try:
#             stats = driver.find_element_by_xpath("//div[@class='ml1-AllStats ml1-AllStats_PosBar ']")
#             stat = stats.text.split(' ')
#             data = [[stat[0].split('\n')[1], stat[0].split('\n')[2]]]
#             data.append([stat[1].split('\n')[1], stat[1].split('\n')[2]])
#             data.append([stat[2].split('\n')[1], stat[2].split('\n')[2]])
#             data.append([stat[3].split('\n')[1], stat[3].split('\n')[2]])
#             data.append([stat[4].split('\n')[1], stat[4].split('\n')[2]])
#             data.append("ads")
#             writer.writerow(data)
#             print(data)
#             count -= 1
#         except:
#             print("error")