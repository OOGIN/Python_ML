from flask import Flask
from flask import request
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'
    
@app.route('/user') 
def user():
    data = pd.read_csv('DATA_01.csv', engine='python')
    df = pd.DataFrame(data)

    y = df['Thrust Speed Average, mm/min']
    X = df.drop(['Thrust Speed Average, mm/min'], axis=1)
    Y=str(y)
    std = StandardScaler()
    X = std.fit_transform(X)
    return str(X)

if __name__ == '__main__':
    app.run(debug=True)