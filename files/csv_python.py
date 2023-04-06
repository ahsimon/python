import csv
import requests

with open('data.csv', mode = "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        response = requests.post("http://url",json=row)
        print("status code: ",  response.status_code,  )
        print("body: ",  response.text,  )
        


