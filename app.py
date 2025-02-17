from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load("model.pkl")
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = []
        
        
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = request.form['applicant_income']
        coapplicant_income = request.form['coapplicant_income']
        loan_amount = request.form['loan_amount']
        loan_amount_term = request.form['loan_amount_term']
        credit_history = request.form['credit_history']
        property_area = request.form['property_area']
        
        
        inputs = [gender, married, dependents, education, self_employed, 
                  applicant_income, coapplicant_income, loan_amount, 
                  loan_amount_term, credit_history, property_area]
        
        for i, input_value in enumerate(inputs):
            if not input_value:
                return render_template('index.html', error=f"Error: All fields must be filled out. Missing value for feature {i+1}.", result=None)
            try:
                features.append(float(input_value))
            except ValueError:
                return render_template('index.html', error=f"Error: Invalid input for feature {i+1}. Please enter a valid number.", result=None)

        
        input_features = np.array(features).reshape(1, -1)
        input_features_scaled = scaler.transform(input_features)

        
        prediction = model.predict(input_features_scaled)

        
        return render_template('index.html', result=f"Prediction Result: {'Loan Approved' if prediction[0] == 1 else 'Loan Denied'}", error=None)
    
    except Exception as e:
        return render_template('index.html', error=str(e), result=None)
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000, debug=True)
