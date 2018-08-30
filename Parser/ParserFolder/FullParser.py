import csv
import time
import sys
import os.path
from selenium import webdriver


driver = webdriver.Chrome('D:/chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')


myData = [["Time"], ["Attacks"], ["Dangerous Attacks"], ["Possession %"], ["On Target"], ["Off Target"], ["League"], ["Command Name"], ["Score"]]

def newLeagueSplitter(leagues):
    splittedCommandByLeague = [[]]
    s = []
    for i in range(len(leagues)):
        league = leagues[i].text.split('\n')
        s.append(league[0])
        for j in range(len(league)):
            if len(league[j]) == 5 and league[j][2] == ':':
                s.append(league[j + 1])
                s.append(league[j + 2])
        splittedCommandByLeague.append(s)
        s = []
    return splittedCommandByLeague


def newWriter(timer, statsTeamOne, statsTeamTwo, moreStatsOne, moreStatsTwo, leagues, commandName, score):

    file_exist = os.path.isfile('D:/MatchDataset/' + commandName[0].text + commandName[1].text + '.csv')
    file = open('D:/MatchDataset/' + commandName[0].text + commandName[1].text + '.csv', 'a+')
    writer = csv.writer(file)
    if file_exist == False:
        writer.writerow(myData)
    data = [timer.text]
    data.append([statsTeamOne[0].text, statsTeamTwo[0].text])
    data.append([statsTeamOne[1].text, statsTeamTwo[1].text])
    if len(statsTeamOne) > 2:
        data.append([statsTeamOne[2].text, statsTeamTwo[2].text])
    else:
        data.append(['0', '0'])
    data.append([moreStatsOne[0].text, moreStatsTwo[0].text])
    data.append([moreStatsOne[1].text, moreStatsTwo[1].text])
    leagues = newLeagueSplitter(leagues)
    leagueName = []
    for i in range(len(leagues)):
        for j in range(len(leagues[i])):
            if [commandName[0].text] == [leagues[i][j]] or [commandName[1].text] == [leagues[i][j]]:
               leagueName.append(leagues[i][0])

    if len(leagueName) > 0:
        data.append([leagueName[0]])
    else:
        data.append(["error"])
    data.append([commandName[0].text, commandName[1].text])
    data.append([score[0].text, score[1].text])
    writer.writerow(data)
    print(data)
    file.close()


while 1:
    time.sleep(5)
    count = 0
    elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")

    for element in elements:
        element.click()
        time.sleep(1)
        try:
            statsTeamOne = driver.find_elements_by_xpath("//div[@class='ml1-StatWheel_Team1Text ']")
            statsTeamTwo = driver.find_elements_by_xpath("//div[@class='ml1-StatWheel_Team2Text ']")
            moreStatsOne = driver.find_elements_by_xpath("//span[@class='ml1-SoccerStatsBar_MiniBarValue"
                                                         " ml1-SoccerStatsBar_MiniBarValue-1 ']")
            moreStatsTwo = driver.find_elements_by_xpath("//span[@class='ml1-SoccerStatsBar_MiniBarValue"
                                                         " ml1-SoccerStatsBar_MiniBarValue-2 ']")
            commandName = driver.find_elements_by_xpath("//div[@class='ml1-ScoreHeader_TeamText ']")
            score = driver.find_elements_by_xpath("//div[@class='ml1-ScoreHeader_Score ']")
            leagues = driver.find_elements_by_xpath("//div[@class='ipo-Competition ipo-Competition-open ']")
            timer = driver.find_element_by_xpath("//span[@class='ml1-ScoreHeader_Clock ']")

            newWriter(timer, statsTeamOne, statsTeamTwo, moreStatsOne, moreStatsTwo, leagues, commandName, score)

        except:
            print("Unexpected error:", sys.exc_info()[0])

    driver.refresh()