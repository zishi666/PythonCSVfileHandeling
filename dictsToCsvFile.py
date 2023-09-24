import csv
data = [
    {
        "OrderID": 1, 
        "Product": "Widget A", 
        "Quantity": 10, 
        "Price": 25.00},
    {
        "OrderID": 2, 
        "Product": "Widget B", 
        "Quantity": 5, 
        "Price": 15.00},
    {
        "OrderID": 3, 
        "Product": "Widget A", 
        "Quantity": 7, 
        "Price": 25.00},
    {
        "OrderID": 4, 
        "Product": "Widget C", 
        "Quantity": 3, 
        "Price": 30.00},
    {
        "OrderID": 5, 
        "Product": "Widget B", 
        "Quantity": 8, 
        "Price": 15.00}
]

name = ', '.join(data[0])
namesfields = name.split(', ')
print(namesfields)

with open('NewStock.csv', 'w') as csvFile:
    writeData = csv.DictWriter(csvFile, fieldnames=namesfields)
    writeData.writeheader()
    for dict in data:
        writeData.writerow(dict)