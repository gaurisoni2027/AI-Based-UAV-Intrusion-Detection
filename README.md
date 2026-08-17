# AI-Based Intrusion Detection for UAV Communication Networks Using Machine Learning and Deep Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![Status](https://img.shields.io/badge/Status-Deployed-success)

An AI-powered Intrusion Detection System (IDS) developed during my **Machine Learning Internship at DRDO**, designed to detect malicious communication patterns in UAV networks using Machine Learning techniques and a real-world cybersecurity dataset.

## Live Demo

**Streamlit Application:** https://ai-based-uav-intrusion-detection.streamlit.app/

---

## Project Overview

Modern **Unmanned Aerial Vehicles (UAVs)** play a critical role in defense applications such as border surveillance, reconnaissance, intelligence gathering, and real-time monitoring. Since UAVs continuously communicate with Ground Control Stations (GCS) over wireless networks, they are vulnerable to cyber attacks that can compromise communication reliability and mission safety.

This project develops an **AI-based Intrusion Detection System (IDS)** capable of classifying UAV network traffic as either normal or malicious by learning patterns from real-world network communication data.

---

## Key Features

- UAV network traffic intrusion detection using Machine Learning.
- Detection of Benign, DoS, and Replay attacks.
- Comprehensive data preprocessing and feature engineering pipeline.
- Exploratory Data Analysis (EDA) of network traffic.
- Comparison of Machine Learning and Deep Learning models.
- Interactive Streamlit Cloud deployment.
- CSV upload interface for real-time prediction.

---

## Live Application

The project is deployed on **Streamlit Cloud**, allowing users to upload a UAV communication dataset and receive real-time intrusion detection results through an interactive dashboard.

### Application Features

- Upload UAV communication datasets in CSV format.
- Detect Benign, DoS, and Replay traffic.
- View packet-wise predictions with confidence scores.
- Monitor attack distribution and threat level through an interactive dashboard.
- Generate a real-time security assessment based on detected attacks.

**Live Demo:** https://ai-based-uav-intrusion-detection.streamlit.app/

---

## Dataset

**Cyber-Physical Dataset for UAVs Under Normal Operations and Cyberattacks (IEEE T-ITS Dataset)**

The dataset contains network traffic collected from a real UAV cyber-physical testbed under both normal flight conditions and multiple cyber attack scenarios.

This project primarily utilizes the **Cyber (Network Communication)** portion of the dataset.

### Attack Categories

Original dataset:

- Benign Communication
- Deauthentication DoS Attack
- Replay Attack
- Evil Twin Attack
- False Data Injection (FDI)

Current implementation:

- Benign Traffic
- DoS Attack
- Replay Attack

The framework is designed to support additional attack categories as future extensions.

---

## Project Objectives

- Analyze the UAV cyber-physical dataset.
- Create a clean network intrusion dataset.
- Perform Exploratory Data Analysis.
- Develop Machine Learning baseline models.
- Compare Deep Learning and Machine Learning approaches.
- Build a deployable intrusion detection application.
- Demonstrate practical defense cybersecurity applications.

---

## Project Workflow

```text
Raw UAV Cyber-Physical Dataset
            │
            ▼
Dataset Understanding
            │
            ▼
Network Dataset Creation
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Data Preprocessing
            │
            ▼
Feature Engineering
            │
            ▼
Machine Learning Models
(Logistic Regression, Random Forest, XGBoost)
            │
            ▼
Deep Learning Models
(MLP, LSTM)
            │
            ▼
Model Evaluation & Comparison
            │
            ▼
Streamlit Cloud Deployment
            │
            ▼
AI-Based UAV Intrusion Detection System
```

---

## Project Structure

```text
AI-Based-UAV-Intrusion-Detection/
│
├── app/
│   ├── app.py
│   └── predict.py
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│   ├── xgboost_final.pkl
│   └── best_lstm_model.pth
│
├── notebooks/
│   ├── 01_dataset_understanding.ipynb
│   ├── 02_dataset_creation.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_preprocessing.ipynb
│   ├── 05_baseline_ml_models.ipynb
│   ├── 06_deep_learning_models.ipynb
│   ├── 07_xgboost_hyperparameter_tuning.ipynb
│   ├── 08_catboost_classifier.ipynb
│   ├── 09_dataset_analysis.ipynb
│   └── 10_feature_selection.ipynb
│
├── sample_data/
├── requirements.txt
└── README.md
```

---

## Model Development

Multiple Machine Learning and Deep Learning models were implemented to evaluate their effectiveness for UAV intrusion detection.

**Models Implemented**

- Logistic Regression – Baseline classifier.
- Random Forest – Ensemble learning baseline.
- CatBoost – Gradient boosting comparison.
- XGBoost – Hyperparameter-optimized model.
- MLP – Deep learning comparison.
- LSTM – Sequential deep learning model.

After comparative evaluation, the optimized **XGBoost** model was selected as the final deployment model due to its superior performance on the processed UAV network dataset.

---

## Model Performance

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 63.71% |
| Random Forest | 72.18% |
| **XGBoost** | **75.65%** |
| MLP | 66.88% |
| LSTM | 67.81% |

The optimized **XGBoost** model achieved the highest overall performance and was deployed in the Streamlit application.

---

## Technologies Used

**Programming**

- Python

**Machine Learning**

- XGBoost
- Scikit-learn
- CatBoost
- PyTorch

**Data Processing**

- Pandas
- NumPy

**Visualization**

- Matplotlib

**Deployment**

- Streamlit Cloud
- Joblib

---

## Future Improvements

- Extend deployment to support Evil Twin and False Data Injection attacks.
- Improve multiclass detection performance through advanced feature engineering.
- Add explainable AI visualizations.
- Support live UAV network traffic monitoring.

---

## Internship

This project was completed during my **Machine Learning Internship at DRDO (Defence Research and Development Organisation)** as part of research-oriented work on AI-driven cybersecurity for UAV communication networks.

---

## Author

**Gauri Soni**

- GitHub: https://github.com/gaurisoni2027
- LinkedIn: https://www.linkedin.com/in/gaurisoni22/