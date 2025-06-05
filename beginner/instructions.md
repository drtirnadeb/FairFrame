## 📘 Beginner Level – Instructions

### 🎯 Objective
Your task is to perform **Exploratory Data Analysis (EDA)** on a loan risk estimation dataset and identify potential **group-level disparities** in loan approvals.

You do **not** need to train any machine learning model for this level. The goal is to analyze the dataset and provide insights into potential unfairness.

---

### 🛠️ Dataset Overview
The dataset is located in `beginner/data/loan_data_full.csv`. It includes:

#### ✅ **Protected attributes** (may be sources of bias):
- `gender`
- `caste`
- `religion`
- `accent_score`

#### ✅ **Neutral attributes** (not expected to introduce bias):
- `age`
- `income`
- `credit_history_score`
- `savings_balance`
- `years_with_bank`
- `number_of_loans`

---

### 🔍 Suggested Explorations
You are encouraged to explore the dataset visually and statistically to identify patterns or disparities. Some helpful analyses:

- **Distributions** of `loan_score` and `approved` across caste, religion, gender, etc.
- **Approval rate comparisons** across protected groups (e.g., SC/ST vs General)
- **Heatmap of correlations** among neutral features to better understand underlying structure
- **Boxplots or scatterplots** to compare loan scores vs. neutral attributes like savings or credit history
- Optional: Calculate **Disparate Impact Ratio** for at least one protected group (formulas provided in intermediate level)

---

### 💡 Example Notebook
A sample notebook `loan_bias_eda.ipynb` is provided as an **example** of the kinds of visualizations and analyses you may perform. You are welcome to go beyond the example and explore the data creatively.

---

### 📈 Deliverables
- A Jupyter notebook containing:
  - Visualizations (histograms, boxplots, heatmaps, etc.)
  - Short commentary on any disparities or patterns you observe
  - Optional but encouraged: one fairness metric (e.g., Disparate Impact Ratio)
