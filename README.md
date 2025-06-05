# ⚖️ FairFrame

**FairFrame** is a modular fairness auditing challenge inspired by real-world use cases in financial services. It is designed to test your ability to detect, quantify, and mitigate algorithmic bias across different AI components. The challenge is organized into three progressive levels—**Beginner**, **Intermediate**, and **Advanced**—each targeting a different part of a fictional fintech company’s AI stack.

---

## 🧠 Scenario: Auditing Banking Access

**Banking Access** is a fictional fintech organization that uses machine learning across:

- 🏦 **Loan Risk Estimator** — predicts loan approval based on user attributes
- 🎯 **Account Promotion Recommender** — targets users with financial product offers
- 💬 **Customer Service Chatbot** — responds to user queries using an LLM

As a fairness auditor, your task is to explore whether these systems behave differently based on **protected attributes** like gender, caste, religion, and accent.

---

## 📁 Repository Structure

```plaintext
FairFrame/
├── beginner/                 # Beginner-level task: EDA and fairness gaps
│   ├── data/loan_data.csv
│   ├── loan_bias_eda.ipynb
│   └── instructions.md
├── intermediate/            # Intermediate-level task: model fairness analysis
│   ├── data/loan_data.csv
│   ├── data/promotion_data.csv
│   ├── intermediate_fairness_analysis.ipynb
│   └── instructions.md
├── advanced/                # Advanced-level task: chatbot bias and LLM scoring
│   ├── data/chatbot_output.csv
│   ├── Advanced_Fairness_Analysis.ipynb
│   └── instructions.md
├── grading_rubric.md        # Grading criteria for each level
├── data_generation/         # Synthetic data generation script
│   └── banking-challenge-data-generation.py
├── README.md
├── projectlog.md            # (Optional) Contributor project log and Git workflow
```

---

## 🟢 Beginner Level

**Focus**: Understand group disparities through exploratory data analysis.

🔑 Tasks:
- Analyze `loan_data.csv` for approval and score differences by gender, caste, religion.
- Use descriptive statistics, bar charts, boxplots, etc.
- Identify patterns or potential biases.

📄 [Beginner Instructions](beginner/instructions.md)  
📊 [Beginner Dataset](beginner/data/loan_data.csv)  
🧪 [Beginner Notebook](beginner/loan_bias_eda.ipynb)

---

## 🟡 Intermediate Level

**Focus**: Train machine learning models and assess fairness with and without protected attributes.

🔑 Tasks:
- Train two models: one **with** and one **without** sensitive features.
- Evaluate fairness metrics: **True Positive Rate (TPR), Demographic Parity, Equal Opportunity**, etc.
- Use both `loan_data.csv` and `promotion_data.csv`.

📄 [Intermediate Instructions](intermediate/instructions.md)  
📊 [Intermediate Datasets](intermediate/data/)  
🧪 [Intermediate Notebook](intermediate/intermediate_fairness_analysis.ipynb)

---

## 🔴 Advanced Level

**Focus**: Use Large Language Models to audit chatbot response fairness.

🔑 Tasks:
- Classify chatbot responses (`chatbot_output.csv`) as *Helpful* or *Generic*
- Use LLM (e.g., Mistral-7B) to rate helpfulness on a scale of 1–5
- Compare helpfulness across groups (caste, gender, etc.)
- Discuss disparities and propose mitigation strategies

📄 [Advanced Instructions](advanced/instructions.md)  
📊 [Advanced Dataset](advanced/data/chatbot_output.csv)  
🧪 [Advanced Notebook](advanced/Advanced_Fairness_Analysis.ipynb)

---

## 🧪 Synthetic Data Generation

All datasets in this repository are **synthetic** and were generated using controlled bias injection logic via:
📜 [`banking-challenge-data-generation.py`](data_generation/banking-challenge-data-generation.py)

Bias was intentionally introduced across **gender**, **caste**, **religion**, and **accent** fields to simulate real-world disparities in prediction outcomes and user experience.

---

## 🧑‍⚖️ Grading and Evaluation

Each level has a corresponding evaluation rubric with qualitative criteria:

📋 [Grading Rubric](grading_rubric.md)

Each submission is assessed based on:
- Correctness and completeness
- Fairness insight and reasoning
- Quality of visualization and communication
- (Advanced) Use of LLMs for response rating and reflection on ethical trade-offs

---

## ✨ Attribution

Created by **Tirna Deb** for a fairness-in-AI design challenge.  
All data and scenarios are fictional and created solely for educational purposes.

---

📝 Note: The dataset also contains queries labeled as `hr_help`, which correspond to a fictional HR chatbot. These are excluded from fairness evaluation in this challenge, as they do not influence loan, promotion, or customer service decisions. However, advanced participants are welcome to explore them optionally.
