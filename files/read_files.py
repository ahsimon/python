import csv
import sys

with open( "random-person.csv", mode = "r") as file :
       reader =csv.reader(file,delimiter=',',quotechar=',')
       for row in reader:
           print(row)     