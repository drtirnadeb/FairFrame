# 🔴 Advanced Task Instructions: Fairness Evaluation and LLM-Assisted Audit

This advanced task builds on the previous Beginner and Intermediate challenges. Participants are expected to **complete the earlier tasks first**, which include:

- **Beginner Level**: Exploratory Data Analysis (EDA) on demographic features, query types, and chatbot responses.
- **Intermediate Level**:
  - Building classification models (e.g., to predict loan outcomes or detect risky users)
  - Creating **fairness-aware versions** of the model: one **with** and one **without protected attributes** (e.g., caste, gender)
  - Computing and comparing fairness metrics across both models (e.g., demographic parity, equal opportunity, TPR, FPR)
  - Interpreting results and summarizing fairness implications.

---

## 🔍 Advanced Task Components

The Advanced Task introduces an additional, qualitative dimension to fairness auditing, leveraging **Large Language Models (LLMs)** to assess **response quality** from the system.

Participants must complete the following:

---

### ✅ 1. Complete Model-Based Fairness Evaluation

Before you begin the chatbot audit, make sure you:

- Train two classification models (with and without protected attributes).
- Compare predictions across demographic subgroups.
- Compute standard **fairness metrics** (e.g., demographic parity, equalized odds).
- Visualize and interpret group-wise disparities.

---

### ✅ 2. Audit the Chatbot Responses Using Human + LLM Evaluation

Now, turn your attention to the **chatbot dataset**.

#### a. Response Quality Classification
- Review user queries and chatbot responses.
- Classify responses as either:
  - **Helpful** (provides a direct, actionable response)
  - **Generic** (vague or deflecting, e.g., “Please visit our FAQ page”)

You may start with rule-based logic, and later move to LLM-assisted evaluation.

#### b. Demographic Bias Assessment
- Group the data by **caste**, **gender**, and **query_type** (focus on financial-service-related queries like `loan_inquiry`, `account_help`).
- Compare helpfulness rates across groups.
- Visualize disparities and flag any response patterns that may indicate unfair treatment.

#### c. LLM-Based Scoring (Advanced)
- Use a large language model (e.g., Mistral-7B-Instruct) to rate the **helpfulness** of chatbot responses on a scale from 1 (unhelpful) to 5 (very helpful).
- Automate this for the full dataset.
- Compare LLM-based helpfulness scores across demographic groups.
- Reflect on differences between rule-based and LLM-based assessments.

---

### ❗ Note on `hr_help` Chatbot

Although the dataset includes queries related to the **HR chatbot** (`hr_help`), you are **not required to analyze it** for this challenge. These responses are considered out of scope for financial service bias auditing and may not affect downstream model fairness outcomes.

---

## 📦 Final Deliverables

Please submit the following:
- One Jupyter Notebook containing:
  - Cleaned code and EDA
  - Model training, fairness metrics, and evaluation plots
  - Chatbot response bias analysis (rule-based + LLM-based)
- A short summary of your findings and recommendations

---

## 💡 Evaluation Criteria

Your submission will be evaluated based on:
- Clarity and structure of your code and analysis
- Correct and thoughtful use of fairness metrics
- Effective comparison of model vs. chatbot bias
- Insightful discussion of ethical implications and mitigation strategies

---

## ✅ Summary Checklist

- [ ] Trained fair and unfair models
- [ ] Compared fairness metrics (across groups)
- [ ] Classified chatbot responses (rule-based)
- [ ] Rated responses using LLM
- [ ] Analyzed disparities across groups
- [ ] Summarized key findings and proposed improvements

