# 🚨 Disaster Relief Aid Prediction System

An AI-powered decision-support system for predicting disaster relief
requirements using historical disaster, population, infrastructure,
and related socio-economic information.

The system combines machine learning with a Flask-based web interface
to estimate the required quantity of relief aid and classify the
appropriate type of assistance for a new disaster scenario.

---

## 📌 Overview

Effective disaster response requires rapid estimation of relief
requirements. Manual assessment can be time-consuming and may be
difficult when large amounts of heterogeneous information need to be
considered.

This project develops a machine-learning-based system that uses
historical disaster and contextual information to support relief
planning.

The trained models are integrated into a Flask web application where
users can provide disaster-related information and obtain predicted
relief requirements.

---

## 🎯 Objectives

- Predict the approximate quantity of relief aid required.
- Classify the appropriate type of relief assistance.
- Use historical disaster information for data-driven prediction.
- Integrate population and infrastructure-related factors.
- Provide an easy-to-use web interface for prediction.
- Support faster and more consistent disaster-response planning.

---

## ✨ Key Features

- 🤖 Machine-learning-based disaster relief prediction
- 📦 Aid quantity prediction
- 🏷️ Aid type classification
- 🌐 Flask-based web application
- 📊 Data preprocessing and feature engineering
- ⚙️ Feature scaling and encoding
- 💾 Pre-trained model integration
- 🖥️ Interactive prediction interface
- 📋 Prediction result page

---

## 🧠 Machine Learning Approach

The system uses two prediction components:

### 1. Aid Quantity Prediction

A regression model is used to estimate the required quantity of
relief aid based on disaster severity and related contextual
features.

The trained model is integrated into the Flask application through
a serialized `.pkl` model file.

### 2. Aid Type Classification

A classification model is used to determine the most appropriate
category/type of assistance based on the characteristics of the
disaster.

The classification pipeline also uses the required preprocessing
and label-encoding artifacts.

---

## 🔄 System Workflow

```text
                ┌─────────────────────┐
                │   User Input        │
                │ Disaster Information│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Data Preprocessing   │
                │ Scaling / Encoding   │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ Aid Quantity    │   │ Aid Type        │
        │ Regression      │   │ Classification  │
        └────────┬────────┘   └────────┬────────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                ┌─────────────────────┐
                │ Prediction Results  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Flask Web Interface │
                └─────────────────────┘
```
---

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Web Framework | Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Data Input | CSV, Excel |
| Frontend | HTML, CSS |
| Development | VS Code |

## 📂 Project Structure
```text 

DISASTER_RELIEF_PROJECT/
│
├── app.py
│
├── aid_quantity_model.pkl
├── aid_type_model.pkl
├── features.pkl
├── label_encoder.pkl
├── scaler.pkl
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── README.md
│
└── templates/
    ├── index.html
    └── result.html
```
## 💾 Dataset
The project uses multiple datasets related to disaster events and contextual information, including:

Historical disaster records
Population data
Infrastructure and health-centre information
Disaster characteristics
Geospatial information
Processed and merged training data
Dataset Availability

The original datasets are not included in this GitHub repository.

They are maintained separately because of their size and to keep the repository lightweight.

The datasets were used locally for:

Data cleaning
Data preprocessing
Feature engineering
Model training
Model evaluation

See data/README.md for information about the expected dataset structure.

The trained machine-learning model artifacts required for the Flask application are included in this repository.

## 📁 Dataset Setup

The original datasets are not included in this repository.

If reproducing the complete training workflow, place the required datasets inside the data/ directory according to the structure described in:

data/README.md

The trained .pkl model files required for running the prediction application are already included in the repository.

## ▶️ Run the Application

After installing the dependencies and ensuring the required model files are present, start the Flask application:

python app.py

Then open the application in a web browser:

http://127.0.0.1:5000

## 📊 Prediction Output

The application provides predictions related to:

Estimated relief aid quantity
Predicted aid type/category

The prediction results are presented through a dedicated result page in the Flask web application.

## 🔬 Project Methodology
```text
The overall machine-learning workflow consists of:

Data Collection
      ↓
Data Cleaning
      ↓
Dataset Integration
      ↓
Feature Engineering
      ↓
Data Preprocessing
      ↓
Feature Scaling / Encoding
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Serialization
      ↓
Flask Integration
      ↓
User Input
      ↓
Prediction
      ↓
Result Visualization
```
## ⚠️ Limitations
Prediction quality depends on the availability and quality of historical disaster data.
The model should be retrained when substantially new disaster patterns or datasets become available.
Predictions are intended to support decision-making and should not replace expert assessment during actual emergency response.
The original training datasets are not distributed with this repository.
Model performance may vary for disaster scenarios that are significantly different from those represented in the training data.

## 🚀 Future Scope

Potential improvements include:

Integration of real-time disaster information
Weather and satellite-data integration
Geographic visualization of affected regions
Advanced ensemble and deep-learning models
Real-time relief demand forecasting
Automated disaster severity assessment
Integration with government disaster-management systems
Explainable AI for prediction transparency
Automated resource allocation recommendations

## 🌍 Potential Applications

The system can potentially support:

Disaster management agencies
Humanitarian organizations
Emergency response planning
Relief-resource allocation
Government disaster-response departments
Disaster risk analysis
Academic research in disaster analytics

## 👩‍💻 Author

Manjot Kaur , Khushpreet Kaur

B.Tech Computer Science & Engineering

## 📄 License

This project was developed for academic and research purposes.
