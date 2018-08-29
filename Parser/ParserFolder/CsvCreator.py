import csv
try:
    file = open('D:/testingcsv1.csv', 'a+')
    writer = csv.writer(file)
    writer.writerow(["asdasdhello"])
    file.close()
    writer.writerow(["asdasdhello"])
except:
    print("Could not open file! Please close Excel!")