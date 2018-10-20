import csv
import time
import sys
import os.path
from selenium import webdriver
import re


driver = webdriver.Chrome(os.path.dirname(os.path.abspath('')) + '\chromedriver1.exe')

driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')
driver.get('https://www.bet365.com/?lng=1&rurl=casino.bet365.com#/IP/')

splittedCoef = [[]]
splittedLeagues = [[]]
iteration = 0

myData = [["Time"], ["Attacks"], ["Dangerous Attacks"], ["Possession %"], ["On Target"], ["Off Target"], ["League"], ["Command Name"], ["Score"],
          ["1x2 First command"], ["1x2 The second command"], ["1x2 Draw"], ["Next goal First command"], ["Next goal second command"], ["Next goal Draw"],
          ["Match goals First command"], ["Match goals The second command"], ["Match goals Draw"]]

def getCoef(league, index):
    coefs = []
    test = league[index - 5]
    for i in range(index, index + 11):
        try:
            if (i < len(league)) and league[i] is not None and not (' ' in league[i]):
                value = float(league[i])
                coefs.append(value)

        except:
            print("Unexpected error:", sys.exc_info()[0])
    for i in range(len(coefs)):
        coefs[i] = str(float(coefs[i]) - 1)
    splittedCoef.append([test, coefs])
    iteration = 1


def newLeagueSplitter(leagues):
    splittedCommandByLeague = [[]]
    s = []
    #t = time.time()

    for i in range(len(leagues)):
        league = re.split("\n", leagues[i].text)
        #league = leagues[i].text.split('\n')
        s.append(league[0])
        #print(s)

        for j in range(len(league)):
            if len(league[j]) == 5 and league[j][2] == ':':
                if iteration == 0:
                    getCoef(league, j + 6)  #+4 because 0 - time +1 - command 1 name +2 - command 2 name +3 - draw
                s.append(league[j + 1])
                s.append(league[j + 2])
        splittedCommandByLeague.append(s)
        s = []

    #print(time.time() - t)
    for i in range(len(splittedCommandByLeague)):
        splittedLeagues.append(splittedCommandByLeague[i])
    print(splittedLeagues)
    #return splittedCommandByLeague


def leagueDetection(leagues, commandName, leagueName):
    for i in range(len(leagues)):
        for j in range(len(leagues[i])):
            if [commandName[0].text] == [leagues[i][j]] or [commandName[1].text] == [leagues[i][j]]:
                leagueName.append(leagues[i][0])
                return leagueName


def newWriter(timer, statsTeamOne, statsTeamTwo, moreStatsOne, moreStatsTwo, leagues, commandName, score):

    file_exist = os.path.isfile('D:/MatchDataset/' + commandName[0].text + commandName[1].text + '.csv')
    file = open('D:/MatchDataset/' + commandName[0].text + commandName[1].text + '.csv', 'a+', newline='')
    writer = csv.writer(file)
    if file_exist == False:
        writer.writerow(myData)
    if len(timer.text) > 0:
        if timer.text == "45:00" or timer.text == "00:00":
            return
        data = [[timer.text]]
    else:
        data = [['00:00']]


    if len(statsTeamOne) > 0:
        data.append([statsTeamOne[0].text, statsTeamTwo[0].text])
        if len(statsTeamOne) > 1:
            data.append([statsTeamOne[1].text, statsTeamTwo[1].text])
            if len(statsTeamOne) > 2:
                data.append([statsTeamOne[2].text, statsTeamTwo[2].text])
            else:
                data.append(['0', '0'])
        else:
            for i in range(0, 2):
                data.append(['0', '0'])
    else:
        for i in range(0, 3):
            data.append(['0', '0'])

    if len(moreStatsOne) > 0:
        data.append([moreStatsOne[0].text, moreStatsTwo[0].text])
        if len(moreStatsOne) > 1:
            data.append([moreStatsOne[1].text, moreStatsTwo[1].text])
        else:
            data.append(['0', '0'])
    else:
        for i in range(0, 2):
            data.append(['0', '0'])

    if len(splittedLeagues) == 1:
        newLeagueSplitter(leagues)
    #print(len(splittedLeagues))
    #print(splittedCoef)

    leagueName = []

    leagueName = leagueDetection(splittedLeagues, commandName, leagueName);

    if len(leagueName) > 0:
        data.append([leagueName[0]])
    else:
        data.append(["error"])
    data.append([commandName[0].text, commandName[1].text])
    data.append([score[0].text, score[1].text])

    for i in range(len(splittedCoef)):
        if len(splittedCoef[i]) > 0 and commandName[0].text == splittedCoef[i][0]:
            for coef in splittedCoef[i][1]:
                data.append([coef])
            break

    writer.writerow(data)
    print(data)
    file.close()


while 1:
    time.sleep(5)
    count = 0
    elements = driver.find_elements_by_xpath("//div[@class='wl-MediaButtonLoader wl-MediaButtonLoader_ML1 ']")

    if len(elements) > 0:
        #delay = 50 / len(elements)
        delay = 1

        for element in elements:
            try:
                element.click()
                time.sleep(delay)
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

                    newWriter(timer, statsTeamOne, statsTeamTwo, moreStatsOne, moreStatsTwo, leagues, commandName,
                              score)


                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    print("error here")
            except:
                print("Unexpected error:", sys.exc_info()[0])

        iteration = 0
        splittedCoef = [[]]

    else:
        soccer = driver.find_elements_by_xpath("//div[@class='ipo-Classification sport_1 ']")
        print(len(soccer))
        if len(soccer) > 0:
            soccer[0].click()
            bar_item = driver.find_elements_by_xpath("//div[@class='ip-ControlBar_BBarItem ']")
            for element in bar_item:
                if element.text == "Overview":
                    element.click();
                    break

    splittedLeagues = [[]]
    driver.refresh()