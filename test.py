from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib

data = pd.read_csv('DATA_01.csv', engine='python')
df = pd.DataFrame(data)

# 데이터 값
y = df['Thrust Speed Average, mm/min']

#데이터 내용
X = df.drop(['Thrust Speed Average, mm/min'], axis=1)

# 변환된 X로 데이터 분할
# 데이터 분리
X_train_org, X_test_org, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# 데이터 전처리
std = StandardScaler()

X_train = std.fit_transform(X_train_org)
X_test = std.transform(X_test_org)

# 그래디언트부스팅 + 그리드서치로 모델 학습
gs = joblib.load('./GradientBoosting_model.pkl')



# 그리드서치 학습 결과 출력
print('베스트 하이퍼 파라미터: {0}'.format(gs.best_params_))
print('베스트 하이퍼 파라미터 일 때 훈련 세트의 정확도 점수: {0:.2f}'.format(gs.best_score_))

model = gs.best_estimator_ #최적화 모델

# 학 습 모델을 현재 경로에 GradientBoosting_model.pkl로 저장

score_GB = model.score(X_test, y_test)
print('테스트세트에서의 정확도 점수: {0:.2f}'.format(score_GB))

# 테스트세트 예측 결과 샘플 출력

predicted_GB = model.predict(X_test)

score = r2_score(y_test, predicted_GB)

print("Mean_absolute_error(MAE):", mean_absolute_error(y_test, predicted_GB))
mse = mean_squared_error(y_test, predicted_GB)
print("mean_squared_error(MSE)", mse)
RMSE = np.sqrt(mse)
print("RMSE(epsilon = 1.5):", RMSE)
print("결정계수(설명력) r2_score:", score)

plt.figure(figsize=(8, 8))

plt.scatter(predicted_GB, y_test,c='gray', edgecolors='w',label='Gradient Boosting Regression \n - R2 score: %.2f' % score)

plt.ylabel('Measured Advance Rate(Test Set), mm/min', fontsize=12)

plt.xlabel('Predicted Advance Rate, mm/min', fontsize=12)

plt.grid(linestyle='--')
plt.legend(loc=2)
plt.xlim([0, 80])
plt.ylim([0, 80])
plt.show()