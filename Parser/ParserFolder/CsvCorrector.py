import csv

input = open("D:/MatchDataset/UWA-Nedlands FC WomenFremantle City FC Women.csv", 'r')
output = open("D:/UWA-Nedlands FC WomenFremantle City FC Women.csv", 'w')
writer = csv.writer(output)
for row in csv.reader(input):
    if len(row) > 1:
        writer.writerow(row)
input.close()
output.close()