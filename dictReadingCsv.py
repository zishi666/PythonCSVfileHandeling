import csv

with open('EmployeeData.csv') as csvFile:
    employeeData = csv.DictReader(csvFile)
    for row in employeeData:
        for key, value in row.items():
            print(key," : ", value)
        print("\n")

with open('EmployeeData.csv', 'r') as csvFile:
    employeeData = csv.DictReader(csvFile)
    lineCount = 0
    for row in employeeData:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        print(f"{row['EmployeeID']}",f"{ row['FirstName']}",f"{ row['LastName']}",f"{ row['Department']}",f"{ row['Salary']}")
    print("\n")

with open('StudentGrades.csv', 'r') as csvFile:
    studentdata = csv.DictReader(csvFile)
    lineCount = 0
    for row in studentdata:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        print(f"{row['StudentID']}",f"{ row['FirstName']}",f"{ row['LastName']}",f"{ row['Math']}",f"{ row['Science']}",f"{ row['English']}")
    print("\n")

with open('SalesData.csv', 'r') as csvFile:
    salesData = csv.DictReader(csvFile)
    lineCount = 0
    for row in salesData:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        print(f"{row['OrderID']}",f"{ row['Product']}",f"{ row['Quantity']}",f"{ row['Price']}")
    print("\n")