from pymongo import MongoClient
from flask import Flask

import pandas as pd

client = MongoClient(host='localhost', port=27017)

# data = pd.read_csv('DATA_01.csv', engine='python')
# df = pd.DataFrame(data)

# lines = str(df).split('\n')

db = client['Py_conn'] # Py_conn 라는 이름의 데이터베이스에 접속
app = Flask(__name__)

@app.route('/act', methods=['GET'])
def act():
    ref={
        "test": "123"
    }
    return ref

# @app.route('/test', methods=['GET'])
# def test():
#     return lines

if __name__ == "__main__":
    app.run()