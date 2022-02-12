import pickle

model = None

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)



X_sample = {'buildYear':2022, 'dong':'잠실동', 'areaForExclusiveUse':30, 'floor':2, 'kinds':'빌라', 'region':'송파구'}
y_sample = model.predict([X_sample])

print(f'최소 약 {str(int(y_sample[0]))[0]}억 {str(int(y_sample[0]))[1]},{str(int(y_sample[0]))[2:]}만 (원) 입니다.')