
from flask import Flask
from flask import request

from sklearn.preprocessing import StandardScaler

import pandas as pd
import joblib

def GetStandardScaler(csv_file_name, drop_column_name):
    data = pd.read_csv(csv_file_name, engine='python')
    df = pd.DataFrame(data)
        
    X = df.drop([drop_column_name], axis=1)
    
    std = StandardScaler()
    X = std.fit_transform(X)
    
    return std



thrust_gs = joblib.load('./GradientBoosting_model.pkl')
thrust_model = thrust_gs.best_estimator_
thrust_std = GetStandardScaler('DATA_01.csv', 'Thrust Speed Average, mm/min')

target_gs = joblib.load('./nonCohesiveSoils01_LGBM_GridSearchCV.pkl')
target_model = target_gs.best_estimator_
target_std = GetStandardScaler('DataSet_nonCohesiveSoils01.csv', 'Target')

app = Flask(__name__)

@app.route("/GetThrustSpeed", methods=['GET'])
def GetThrustSpeed():
    arg_arr = {
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
    df = pd.DataFrame(arg_arr)
    conv_data = thrust_std.transform(df)
    predicted_value = thrust_model.predict(conv_data)

    return str(predicted_value[0])
        
@app.route("/GetTarget", methods=['GET'])
def GetTarget():
    arg_arr = {
        'Thrust Speed Average':[request.args['tsa']],
        'Total thrust force':[request.args['ttf']],
        'Screw revolution':[request.args['sr']],
        'Cutter Torque':[request.args['ct']],
        'Screw Torque':[request.args['st']],
        'Soil Pressure':[request.args['sp']],
    }
    df = pd.DataFrame(arg_arr)
    conv_data = target_std.transform(df)
    predicted_value = target_model.predict(conv_data)

    return str(predicted_value[0])

if __name__=='__main__':
    app.run(debug=True)