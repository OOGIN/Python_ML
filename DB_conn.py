import csv 
from pymongo import MongoClient

mongoClient = MongoClient()
db = mongoClient['py_conn']
collection = db['test1']

header = ['usc', 'lv', 'nva', 'ttf', 'asjs', 'srm', 'ctm', 'stm', 'cs', 'gs', 'sp', 'tns']
csvFile = open('DATA_01.csv', 'r')
reader = csv.DictReader(csvFile)

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    collection.insert(row)