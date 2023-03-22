from flask import Flask
from flask import request
from sklearn.preprocessing import StandardScaler

import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/act', methods=['GET'])
def act():
    ref={
        "student":[
        {"name":"kim", "age":30},
        {"name":"lee", "age":20}
        ]
    }
    return ref

@app.route('/Testingroom', methods=['POST'])
def test():
    ref={}
    return ref

if __name__ == "__main__":
    app.run()