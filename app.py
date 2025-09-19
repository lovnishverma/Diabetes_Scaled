from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
import datetime
import pytz

app = Flask(__name__)

# Load saved model and scaler (make sure you saved both during training)
model = joblib.load("diabetes_model.joblib")
scaler = joblib.load("scaler.joblib")   # load the same scaler used in training


@app.route('/')
def home():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    # greet user according to Time
    hour = current_time.hour
    if 5 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    greeting = greeting
    # rendering the home page
    return render_template('index.html', greet=greeting, title="Homepage")


@app.route('/form')
def form():
    # rendering the prediction form page
    return render_template('predict.html', title="Predict Diabetes")


@app.route('/predict', methods=['POST'])
def predict_form():
    # Get user input
    Pregnancies = int(request.form.get("Pregnancies"))
    Glucose = float(request.form.get("Glucose"))
    BloodPressure = float(request.form.get("BloodPressure"))
    SkinThickness = float(request.form.get("SkinThickness"))
    Insulin = float(request.form.get("Insulin"))
    BMI = float(request.form.get("BMI"))
    DiabetesPedigreeFunction = float(
        request.form.get("DiabetesPedigreeFunction"))
    Age = int(request.form.get("Age"))

    # Arrange user input into numpy array
    user_input = np.array([[Pregnancies, Glucose, BloodPressure,
                            SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age]])

    # Scale input using pre-fitted scaler
    user_input_scaled = scaler.transform(user_input)

    # Make prediction
    prediction = model.predict(user_input_scaled)[0]
    probability = model.predict_proba(user_input_scaled)[0][prediction] * 100

    # Format result
    if prediction == 1:
        result = f"The person is Diabetic (Confidence: {probability:.2f}%)"
    else:
        result = f"The person is Non-Diabetic (Confidence: {probability:.2f}%)"

    return render_template('predict.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
