from pymongo import MongoClient
from flask import request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

client = MongoClient("mongodb://localhost:27017/")

db = client['Py_conn'] 

def GetStandardScaler(csv_file_name, drop_column_name):
    data = pd.read_csv(csv_file_name, engine='python')
    df = pd.DataFrame(data)
        
    X = df.drop([drop_column_name], axis=1)
    
    std = StandardScaler()
    X = std.fit_transform(X)
    
    return std


data = {
    'author' : 'hun',
    'text' : 'mongoDB is what..?',
    'tags' : ['mongoDB', 'python', 'pymongo']
}


dpInsert = db.tests.insert_one(data)

# for datas in db['csv1'].find({}):
#     print(datas)