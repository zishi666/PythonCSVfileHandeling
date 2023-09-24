import csv
with open('ThisStock.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        keyList = ', '.join(row)
        keyList = keyList.split(', ')
        break
with open('ThisStock.csv', 'a', newline='\n') as csvFile:
    dataWriter = csv.DictWriter(csvFile, fieldnames=keyList)
    dataWriter.writerow({f"{keyList[0]}":7,f"{keyList[1]}":"Product Nth",f"{keyList[2]}":15,f"{keyList[3]}":55.0})
    print("data appended seccusfully...!")