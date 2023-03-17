from pymongo import MongoClient
import datetime


client = MongoClient(host='localhost', port=27017)

db = client['Py_conn'] # Py_conn 라는 이름의 데이터베이스에 접속

data = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

# posts 라는 이름의 컬렉션을 만들어 data 삽입
# db['posts']
dpInsert = db.posts.insert_one(data)

for d in db['posts'].find():
    print(d['author'], d['text'], d['tags'])

# hun mongoDB is what..? ['mongoDB', 'python', 'pymongo']
# lee Who are you? ['person', 'lee']

# text 칼럼을 제외하고 데이터 가져오기
for d in db['posts'].find({}, {'text' : 0}):
    print(d)