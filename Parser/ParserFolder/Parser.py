import csv
import time
import sys
import os.path
from selenium import webdriver


driver = webdriver.Chrome('D:/chromedriver1.exe')

driver.get('https://mobile.bet365.com/#type=InPlay;key=;ip=1;lng=1')

myData = [["Time"], ["Attacks"], ["Dangerous Attacks"], ["Possession %"], ["On Target"], ["Off Target"], ["League"], ["Command Name"], ["Score"]]


def leagueSplitter(league):
    league = league.text.split('\n')
    splittedCommandByLeague =[[]]
    s = []
    for i in range(len(league)):
        if len(league[i]) > 5:
            s.append(league[i])
        elif len(league[i]) == 5 or len(league[i]) == 3 or len(league[i]) == 4:
            if len(league[i+1]) > 5 and len(league[i+3]) < 5:
                splittedCommandByLeague.append(s)
                s = []
    return splittedCommandByLeague


def writer(stats, scores, league):
    try:
        score = scores.text.split('\n')
        stat = stats.text.split(' ')
        league = leagueSplitter(league)

        file_exist = os.path.isfile('D:/MatchDataset/' + score[0].split('\n')[0] + score[3].split('\n')[0] + '.csv')
        file = open('D:/MatchDataset/' + score[0].split('\n')[0] + score[3].split('\n')[0] + '.csv', 'a+')
        writer = csv.writer(file)
        if file_exist == False:
            writer.writerow(myData)
        data = [[score[4].split('\n')[0]]]
        data.append([stat[0].split('\n')[1], stat[0].split('\n')[2]])
        data.append([stat[1].split('\n')[1], stat[1].split('\n')[2]])
        data.append([stat[2].split('\n')[1], stat[2].split('\n')[2]])
        data.append([stat[3].split('\n')[1], stat[3].split('\n')[2]])
        data.append([stat[4].split('\n')[1], stat[4].split('\n')[2]])

        leagueName = []
        for i in range(len(league)):
            for j in range(len(league[i])):
                if score[0].split('\n'[0]) == [league[i][j]] or score[3].split('\n'[0]) == [league[i][j]]:
                    leagueName.append(league[i][0])

        if len(leagueName) > 0:
            data.append([leagueName[0]])
        else:
            data.append(["error"])
        data.append([score[0].split('\n'[0]), score[3].split('\n'[0])])
        data.append([score[1].split('\n'[0]), score[2].split('\n'[0])])
        writer.writerow(data)
        print(data)
        file.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])


while 1:
    time.sleep(5)
    count = 0
    elements = driver.find_elements_by_xpath("//div[@class='ipo-ViewSelectorContainer ipo-ViewSelectorContainer_Cid-1 "
                                             "ipo-ViewSelectorContainer_MatchLive ']")
    try:
        stats = driver.find_element_by_xpath("//div[@class='ml1-AllStats ml1-AllStats_PosBar ']")
        score = driver.find_element_by_xpath("//div[@class='ml1-ScoreHeader']")
        league = driver.find_element_by_xpath("//div[@class='ipo-FixtureList ipo-FixtureList_PC-3 ']")
        writer(stats, score, league)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    for element in elements:
        try:
            elements[count].click()
            count += 1
            time.sleep(1)
            try:
                stats = driver.find_element_by_xpath("//div[@class='ml1-AllStats ml1-AllStats_PosBar ']")
                score = driver.find_element_by_xpath("//div[@class='ml1-ScoreHeader']")
                league = driver.find_element_by_xpath("//div[@class='ipo-FixtureList ipo-FixtureList_PC-3 ']")
                writer(stats, score, league)
            except:
                print("Unexpected error:", sys.exc_info()[0])
            time.sleep(1)
            if count == len(elements):
                elements = driver.find_elements_by_xpath(
                    "//div[@class='ipo-ViewSelectorContainer ipo-ViewSelectorContainer_Cid-1 "
                    "ipo-ViewSelectorContainer_MatchLive ']")
                elements[0].click()
                break
        except:
            print("error here")

    driver.refresh()