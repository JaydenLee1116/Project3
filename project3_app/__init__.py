from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = None

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/result', methods=['POST'])
def result():
    data_year = request.form['year']
    data_kinds = request.form['kinds']
    data_gu = request.form['gu']
    data_dong = request.form['dong']
    data_area = request.form['area']
    data_floor = request.form['floor']
    
    X_sample = {'buildYear':data_year, 'dong':data_dong, 'areaForExclusiveUse':data_area, 'floor':data_floor, 'kinds':data_kinds, 'region':data_gu}
    y_pred = model.predict([X_sample])
    # print(f'최소 약 {str(int(y_pred[0]))[0]}억 {str(int(y_pred[0]))[1]},{str(int(y_pred[0]))[2:]}만 (원) 입니다.')

    return render_template('result.html', data_uk=str(int(y_pred[0])//10000), data_chun=str((int(y_pred[0])%10000))[0], data_last=str((int(y_pred[0])%10000))[1:]), 200

# if __name__ == "__main__":
#     app.run(debug=True)