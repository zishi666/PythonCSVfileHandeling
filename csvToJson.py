import csv, json
array = []
with open('ThisStock.csv', 'r') as csvFile:
    fileReader = csv.DictReader(csvFile)
    with open('JsonFile.json', 'a') as jsonFile:
        for dicti in fileReader:
            array.append(dicti)
        json.dump(array, jsonFile, indent=4)
        