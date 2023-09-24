import os, csv
with open('ThisStock.csv', 'r') as MainFile, open('Temp.csv', 'w') as NewFile:
    MainFileData = csv.DictReader(MainFile)
    NewFileWriter = csv.DictWriter(NewFile, fieldnames=MainFileData.fieldnames)
    NewFileWriter.writeheader()
    for dict in MainFileData:
        if float(dict['Price']) <= 40.00:
            dict['Price'] = float(input(f'Enter new Price of {dict["Product"]} => '))
            NewFileWriter.writerow(dict)
        else:
            NewFileWriter.writerow(dict)           
os.remove('ThisStock.csv')
os.rename('Temp.csv', 'ThisStock.csv')