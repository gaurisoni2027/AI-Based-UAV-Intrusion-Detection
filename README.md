# AI-Based Intrusion Detection for UAV Communication Networks Using Machine Learning and Deep Learning

## Project Description

Modern Unmanned Aerial Vehicles (UAVs) are extensively used in defense applications such as border surveillance, reconnaissance, intelligence gathering, and real-time monitoring. As these UAVs continuously communicate with Ground Control Stations (GCS) over wireless networks, they become vulnerable to various cyber threats.

This project aims to develop an **Artificial Intelligence-based Intrusion Detection System (IDS)** capable of identifying malicious communication patterns in UAV networks using Machine Learning and Deep Learning techniques. The goal is to accurately distinguish normal UAV communication from cyber attacks using real-world network traffic data.

---

## Dataset

**Cyber-Physical Dataset for UAVs Under Normal Operations and Cyberattacks (IEEE T-ITS Dataset)**

The dataset contains network traffic collected from a real UAV cyber-physical testbed under both normal flight conditions and multiple cyber attack scenarios.

For this project, the **Cyber (Network Communication) Dataset** is used to develop the intrusion detection system.

---

## Attack Categories

The original dataset contains the following attack scenarios:

- Benign Communication
- Deauthentication Denial-of-Service (DoS) Attack
- Replay Attack
- Evil Twin Attack
- False Data Injection (FDI) Attack

The current implementation focuses on the processed network dataset containing:

- Benign Traffic
- DoS Attack
- Replay Attack

Support for Evil Twin and False Data Injection attacks can be incorporated as future extensions.

---

## Project Objectives

- Understand and analyze the UAV cyber-physical dataset.
- Prepare a clean network intrusion dataset for model development.
- Perform comprehensive Exploratory Data Analysis (EDA).
- Build baseline Machine Learning models.
- Develop Deep Learning models for intrusion detection.
- Compare the performance of different models using standard evaluation metrics.
- Build a research-oriented intrusion detection pipeline suitable for defense cybersecurity applications.

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
Exploratory Data Analysis (EDA)
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
(LSTM)
            │
            ▼
Model Evaluation & Comparison
            │
            ▼
AI-Based UAV Intrusion Detection System