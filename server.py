from flask import Flask
from flask import request

from sklearn.preprocessing import StandardScaler

import pandas as pd
import joblib

def GetStandardScaler(csv_name, drop_name):
    data = pd.read_csv(csv_name, engine='python')
    df = pd.DataFrame(data)
    
    X = df.drop([drop_name], axis=1)

    std = StandardScaler()
    X = std.fit_transform(X)
    return std

gs = joblib.load("./GradientBoosting_model.pkl")
model = gs.best_estimator_
thrust_std = GetStandardScaler('DATA_01.csv', 'Thrust Speed Average, mm/min')

app = Flask(__name__)

@app.route('/act', methods=['GET'])
def act():
    ret = {
        'USCSID':[request.args['usc']],
        'lv':[request.args['lv']],
        'Nvalue':[request.args['nva']],
        'Total thrust force, MN':[request.args['ttf']],
        '[99] Average shield jack stroke':[request.args['asjs']],
        'No.1 Screw revolution, min-1':[request.args['srm']],
        'Cutter Torque, MN-m':[request.args['ctm']],
        'No.1 Screw Torque, MN-m':[request.args['stm']],
        '[58] Cutter Speed':[request.args['cs']],
        '[66] No.1 Gate stroke':[request.args['gs']],
        'Soil Pressure, kPa':[request.args['sp']],
        '[628] Thrust Num Selected':[request.args['tns']]
    }
    return 

if __name__ == "__main__":
    app.run()