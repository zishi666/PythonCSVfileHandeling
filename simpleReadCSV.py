import csv

print("Employee Data")
with open('EmployeeData.csv', 'r') as csvfile:
    employeeData = csv.reader(csvfile, delimiter=',')
    lineCount = 0
    for row in employeeData:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        else:
            print(f"{row[0]} : ", f"{row[1]} : ", f"{row[2]} : ", f"{row[3]}")
            lineCount +=1
    print("\n")

print("Student Grades are")
with open('StudentGrades.csv', 'r') as csvfile:
    studenData = csv.reader(csvfile, delimiter=',')
    lineCount = 0
    for row in studenData:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        else:
            print(f"{row[0]} : ", f"{row[1]} : ", f"{row[2]} : ", f"{row[3]} : ", f"{row[4]}")
    print("\n")
        
print("Sales Are as")
with open('SalesData.csv', 'r') as csvFile:
    salesData = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in salesData:
        if lineCount == 0:
            print(f"{', '.join(row)}")
            lineCount += 1
        else:
            print(f"{row[0]} : ", f"{row[1]} : ", f"{row[2]} : ", f"{row[3]}")
    print("\n")    

