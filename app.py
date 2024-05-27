from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Pickles
with open('modely1.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open('modely2.pkl', 'rb') as f:
    model2 = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])

def home():

    if request.method == 'POST':
        # Get the values from the html
        value1 = float(request.form['value1'])
        value2 = float(request.form['value2'])
        value3 = float(request.form['value3'])
        value4 = float(request.form['value4'])
        value5 = float(request.form['value5'])
        value6 = float(request.form['value6'])
        value7 = float(request.form['value7'])
        value8 = float(request.form['value8'])
        value9 = float(request.form['value9'])
        value10 = float(request.form['value10'])
        value11 = float(request.form['value11'])

        # Predict with the new values
        input_features = np.array([[value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11]])
        prediction1 = model1.predict(input_features)
        prediction2 = model2.predict(input_features)
        
        return f"Prediction1: {prediction1[0]}, Prediction2: {prediction2[0]}"
    
    return render_template('index.html')


    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
