import csv
with open('SalesData.csv', 'r') as csvFile:
    salesData = csv.DictReader(csvFile)
    lineCount = 0
    for dict in salesData:
        if lineCount == 0:
            print(f"{', '.join(dict)}")
            lineCount += 1
        if dict['Price'] == '15.00':
            print(f"{dict['OrderID']}     ",f"{dict['Product']}       ",f"{dict['Quantity']}    ",f"{dict['Price']}") 