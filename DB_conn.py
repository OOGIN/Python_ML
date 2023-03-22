import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['Py_conn']

mycol = mydb["json"]

x = mycol.find_one()

print(x)