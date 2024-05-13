from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("D:\Diamond Price Prediction\Pickle File\Decision Tree Regressor.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    carat = float(request.form['carat'])
    cut = int(request.form['cut'])
    color = int(request.form['color'])
    clarity = int(request.form['clarity'])
    depth = float(request.form['depth'])
    table = float(request.form['table'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    
    prediction = model.predict([[carat, cut, color, clarity, depth, table, x, y, z]])
    predicted_price = round(prediction[0], 2)
    
    return render_template('index.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)