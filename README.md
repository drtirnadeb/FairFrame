# FairFrame

FairFrame is a modular fairness auditing challenge inspired by real-world issues in financial services and machine learning systems. It is structured in three levels—Beginner, Intermediate, and Advanced—to simulate bias detection across AI components used by a fictional fintech company.

## 🧠 Challenge Scenario

Banking Access, a fictional company, uses AI/ML systems across:

Loan Risk Estimator (credit scoring)

Account Promotion Recommender (targeted offers)

Customer Service Chatbot (LLM-based)

Participants are invited to audit these systems step by step for potential biases across protected attributes such as gender, caste, religion, and accent.

## 📂 Repository Structure

```
FairFrame/
├── README.md
├── beginner/
│   ├── data/loan_data.csv
│   └── instructions.md
├── intermediate/
│   ├── data/loan_data.csv
│   ├── data/promotion_data.csv
│   └── instructions.md
├── advanced/
│   ├── data/loan_data.csv
│   ├── data/promotion_data.csv
│   ├── data/chatbot_output.csv
│   └── instructions.md
├── data_generation/
│   └── banking-challenge-data-generation.py
├── project-log.md
├── grading-rubic.md

```

## 🔹 Levels

## 🟢 Beginner

Explore `loan_data.csv`

Identify disparities in loan scoring and approval rates

Use descriptive stats and basic visualizations

## 🟡 Intermediate

Add analysis of `promotion_data.csv`

Compare promotion distributions by group

Evaluate bias across two systems

## 🔴 Advanced

Incorporate `chatbot_output.csv`

Score LLM-based chatbot replies for bias

Consider fairness trade-offs across multiple systems

## 📊 Dataset Notes

All datasets are synthetic and were generated using the script in data_generation/. Biases were manually injected for gender, caste, and religion in scores and exposure.

## ✨ Attribution

Created by Tirna Deb for a fairness-in-AI design challenge. This is a fictional problem not associated with any real entity.

