import csv

f = open('csv_file.csv', 'w')

writer = csv.writer(f)
rows = ['name','age']  
writer.writerow (rows)

f.close()
