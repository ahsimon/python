import sys
import csv
from faker import Faker


fake = Faker()
number_of_records=int(sys.argv[1])
  

with open('random-person.csv',mode='w') as file:

    writer = csv.writer(file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['first-name','last-name','age'])

    for _ in range(number_of_records):
        writer.writerow([fake.first_name(),fake.last_name(),fake.numerify("@#")])

