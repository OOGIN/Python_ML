from pymongo import MongoClient
import datetime


client = MongoClient(host='localhost', port=27017)

db = client['Py_conn'] # Py_conn 라는 이름의 데이터베이스에 접속

data = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

# 원하는 이름의 컬렉션을 만들어 data 삽입
dpInsert = db.tests.insert_one(data)

for d in db['tests'].find():
    print(d['author'], d['text'], d['tags'])

# text 칼럼을 제외하고 데이터 가져와서 리스트로 묶기
for d in db['tests'].find({}, {'text' : 0}):
    print(d)