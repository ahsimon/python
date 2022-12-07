import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Mexico', 652090, 'MX', 'MEX']
data1 = ['India', 352090, 'IND', 'IND']

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    writer.writerow(data)
    writer.writerow(data1)