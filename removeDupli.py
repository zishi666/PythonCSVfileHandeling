import csv, os
uniqueList = []
with open('ThisStock.csv', 'r') as currentFile, open('Temp.csv', 'w') as TempFile:
    currentData = csv.DictReader(currentFile)
    tempData = csv.DictWriter(TempFile, fieldnames=currentData.fieldnames)
    tempData.writeheader()
    for dicti in currentData:
        if dicti not in uniqueList:
            uniqueList.append(dicti)
    for itemDict in uniqueList:
        tempData.writerow(itemDict)
os.remove('ThisStock.csv')
os.rename('Temp.csv','ThisStock.csv')