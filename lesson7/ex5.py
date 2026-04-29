import json
import csv

with open ('employees.json', 'r') as f:
    print(json.load(f))
with open ('emp.csv') as c:
    file_write = csv.reader(c, delimiter=",")