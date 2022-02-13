import pickle
import numpy as np
model = None

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


a = 2022
b= '잠실동'
c = 30
d = 16
e = '아파트'
f = '송파구'
X_sample = {'buildYear': a, 'dong':b, 'areaForExclusiveUse':c, 'floor':d, 'kinds':e, 'region':f}
# X_sample = np.array([2022, '잠실동', 30, 16, '아파트', '송파구'])
y_sample = model.predict([X_sample])

print(f'최소 약 {str(int(y_sample[0]))[0]}억 {str(int(y_sample[0]))[1]},{str(int(y_sample[0]))[2:]}만 (원) 입니다.')