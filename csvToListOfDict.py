import csv
################        IN MULTIPLE LISTS       #####################
employeeList = []
with open('EmployeeData.csv', 'r') as csvFile:
    employeeDicts = csv.DictReader(csvFile)
    for row in employeeDicts:
        employeeList.append(row)
    print(employeeList, "\n")

studentList = []
with open('StudentGrades.csv', 'r') as csvFile:
    studentDicts = csv.DictReader(csvFile)
    for dict in studentDicts:
        studentList.append(dict)
    print(studentList, "\n")

salesList = []
with open('SalesData.csv', 'r') as csvFile:
    salesDicts = csv.DictReader(csvFile)
    for dict in salesDicts:
        salesList.append(dict)
    print(salesList, "\n")

########################    IN A SINGLE LIST      #####################

AllDictionaryList = []
employee = {'employee':[]}
with open('EmployeeData.csv', 'r') as csvFile:
    employeeDicts = csv.DictReader(csvFile)
    for dict in employeeDicts:
        employee["employee"].append(dict)
    AllDictionaryList.append(employee)

students = {'students':[]}
with open('StudentGrades.csv', 'r') as csvFile:
    studentDicts = csv.DictReader(csvFile)
    for dict in studentDicts:
        students['students'].append(dict)
    AllDictionaryList.append(students)

sales = {'sales':[]}
with open('SalesData.csv', 'r') as csvFile:
    salesDicts = csv.DictReader(csvFile)
    for dict in salesDicts:
        sales['sales'].append(dict)
    AllDictionaryList.append(sales)
    
print(AllDictionaryList)
