# 🩺 Diabetes Prediction Web Application

A machine learning-powered web application that predicts diabetes risk based on medical parameters. Built with Flask, scikit-learn, and deployed on Hugging Face Spaces.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-yellow)](https://lovnishverma-diabetes-prediction-joblib.hf.space/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)](https://scikit-learn.org/)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [File Structure](#file-structure)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a diabetes prediction system using the famous **PIMA Indians Diabetes Dataset**. The application uses a pre-trained machine learning model to predict whether a person is likely to have diabetes based on various medical parameters.

### Key Highlights:
- ✅ **Beginner-friendly** Flask web application
- ✅ **No Bootstrap** - Pure HTML/CSS for simplicity
- ✅ **Template inheritance** using base.html for clean code
- ✅ **Pre-trained ML model** saved using joblib
- ✅ **Real-time predictions** with confidence scores
- ✅ **Responsive web interface** with time-based greetings
- ✅ **Deployed on Hugging Face Spaces** for easy access

## ⭐ Features

- **Interactive Web Interface**: User-friendly form to input medical parameters
- **Time-based Greetings**: Dynamic greetings based on Indian Standard Time (IST)
- **Real-time Predictions**: Instant diabetes risk assessment
- **Confidence Scores**: Probability percentages for predictions
- **Simple & Clean Design**: No Bootstrap - pure HTML/CSS for better learning
- **Template Inheritance**: Uses Flask's Jinja2 templating with base.html
- **Mobile Responsive**: Works seamlessly on all devices
- **Error Handling**: Robust input validation and error management

## 🚀 Demo

### Live Application
🌐 **[Try the Live Demo](https://lovnishverma-diabetes-prediction-joblib.hf.space/)**

### Source Code
📄 **[Hugging Face Space](https://huggingface.co/spaces/LovnishVerma/diabetes-prediction-joblib)**

### Screenshots

<img width="1902" height="1078" alt="image" src="https://github.com/user-attachments/assets/e19fa271-8990-4cb5-b548-2ab6d3d40d4e" />


## 📊 Dataset

This project uses the **PIMA Indians Diabetes Dataset**, [View Raw](https://raw.githubusercontent.com/lovnishverma/datasets/refs/heads/main/diabetes_new.csv) which contains medical information about Pima Indian women and their diabetes status.

### Features Used:
1. **Pregnancies**: Number of times pregnant
2. **Glucose**: Plasma glucose concentration (mg/dL)
3. **Blood Pressure**: Diastolic blood pressure (mm Hg)
4. **Skin Thickness**: Triceps skinfold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg/(height in m)²)
7. **Diabetes Pedigree Function**: Diabetes pedigree function score
8. **Age**: Age in years

### Target Variable:
- **Outcome**: 0 (Non-diabetic) or 1 (Diabetic)

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lovnishverma/Diabetes_Scaled.git
   cd Diabetes_Scaled
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, install packages manually:
   ```bash
   pip install flask scikit-learn joblib numpy pytz
   ```

4. **Ensure model files are present**
   Make sure these files are in your project directory:
   - `diabetes_model.joblib` (trained ML model)
   - `scaler.joblib` (fitted StandardScaler)

## 🚀 Usage

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Using the Application**
   - Visit the homepage to see the time-based greeting
   - Click on "Predict Diabetes" or go to `/form`
   - Fill in the medical parameters
   - Click "Predict" to get results

### Input Parameters Guide

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| Pregnancies | Number of pregnancies | 0-17 |
| Glucose | Blood glucose level | 50-200 mg/dL |
| Blood Pressure | Diastolic BP | 40-120 mmHg |
| Skin Thickness | Triceps fold | 10-60 mm |
| Insulin | Serum insulin | 15-300 μU/mL |
| BMI | Body Mass Index | 15-50 kg/m² |
| Diabetes Pedigree | Genetic factor | 0.1-2.5 |
| Age | Age in years | 21-80 |

## 🧠 Model Details

### Model Training
The machine learning model was trained using the process documented in this Jupyter notebook:
📓 **[Model Training Notebook](https://github.com/lovnishverma/Python-Getting-Started/blob/main/PIMA_Indians_Diabetes_Classification.ipynb)**

### Design Philosophy
This project follows a **beginner-friendly approach**:
- **No CSS frameworks** like Bootstrap to keep the code simple and understandable
- **Pure HTML/CSS** so beginners can learn fundamental web development concepts
- **Template inheritance** using `base.html` to demonstrate Flask's Jinja2 templating
- **Clean, readable code** with extensive comments for learning purposes

### Model Pipeline
1. **Data Preprocessing**: StandardScaler for feature normalization
2. **Model Training**: Classification algorithm (details in training notebook)
3. **Model Persistence**: Saved using joblib for production use

### Performance
- The model provides probability scores for predictions
- Confidence levels are displayed as percentages
- Both model and scaler are saved for consistent preprocessing

## 📁 File Structure

```
Diabetes_Scaled/
├── app.py                 # Main Flask application
├── diabetes_model.joblib  # Trained ML model
├── scaler.joblib         # Fitted StandardScaler
├── templates/            # HTML templates
│   ├── index.html       # Homepage template
│   └── predict.html     # Prediction form template
├── static/              # CSS, JS, images (if any)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage with greeting |
| `/form` | GET | Prediction form page |
| `/predict` | POST | Process form and return prediction |

### Example API Usage

```python
import requests

# Prediction endpoint
url = "http://localhost:5000/predict"
data = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 25,
    "Insulin": 80,
    "BMI": 25.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 30
}

response = requests.post(url, data=data)
print(response.text)
```

## 🌐 Deployment

### Local Development
```bash
python app.py
# Server runs on http://localhost:5000
```

### Production Deployment Options

1. **Hugging Face Spaces** (Current deployment)
   - Fork the [Hugging Face Space](https://huggingface.co/spaces/LovnishVerma/diabetes-prediction-joblib)
   - Modify files and push changes

2. **Heroku**
   - Add `Procfile`: `web: python app.py`
   - Configure port: `app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))`

3. **Docker**
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Areas for Contribution
- 🎨 Improve UI/UX design (keeping it simple and framework-free)
- 📱 Enhance mobile responsiveness with pure CSS
- 🔍 Add data visualization
- 🧪 Improve model accuracy
- 📚 Add more documentation and code comments
- 🎓 Create beginner tutorials
- 🐛 Fix bugs and issues

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Lovnish Verma**
- GitHub: [@lovnishverma](https://github.com/lovnishverma)
- Hugging Face: [@LovnishVerma](https://huggingface.co/LovnishVerma)

## 🙏 Acknowledgments

- **PIMA Indians Diabetes Dataset** for providing the data
- **Flask** team for the excellent web framework
- **scikit-learn** community for machine learning tools
- **Hugging Face** for free hosting platform

## 📞 Support

If you have any questions or need help:

1. **GitHub Issues**: [Create an issue](https://github.com/lovnishverma/Diabetes_Scaled/issues)
2. **Discussion**: Start a discussion in the repository
3. **Email**: Contact through GitHub profile

---

⭐ **If you found this project helpful, please give it a star!** ⭐

## 📈 Future Enhancements

- [ ] Add data visualization charts
- [ ] Implement user authentication
- [ ] Add prediction history
- [ ] Create REST API documentation
- [ ] Add unit tests
- [ ] Implement model retraining pipeline
- [ ] Add more ML models for comparison
- [ ] Create mobile app version

---

*Last updated: September 2025*

