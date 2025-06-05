## 🧪 Intermediate Challenge Instructions

In this level, your goal is to explore **group-level disparities** in both **loan approval** and **promotion exposure**, combining EDA and fairness-aware ML modeling.

---

### 📘 About the Notebook

We have included an example Jupyter notebook (`loan_fairness_intermediate.ipynb`) to help you get started.  
Use it as a **template** — feel free to build on it, expand the analysis, and apply the same techniques to the promotion dataset.

---

### 🔍 1. Exploratory Data Analysis (EDA)

Begin with data understanding:
- Explore distributions of **protected attributes**: `caste`, `religion`, `gender`
- Examine **neutral features**: `credit_history_score`, `number_of_loans`, `savings_balance`, etc.
- Visualize group-level statistics using:
  - Bar plots
  - Countplots
  - Correlation heatmaps

✅ Tip: Replicate or build on the visualizations provided in the Beginner notebook to support your fairness analysis.

---

### 🤖 2. Train and Compare ML Models (Loan Dataset)

Use the `loan_df` to predict the `approved` outcome.

Train **two models**:
- **With protected attributes** (e.g., `caste`, `religion`, `gender`)
- **Without protected attributes** (only neutral features)

Suggested models:
- Logistic Regression
- Decision Tree Classifier

Evaluate model performance using:
- Accuracy
- Confusion Matrix

⚠️ Note: This is a synthetic dataset, so perfect accuracy may indicate it's too simple or that bias is encoded in correlated non-protected features.

---

### 📊 3. Fairness Metrics (Loan + Promotion)

Calculate **group fairness metrics** for both `loan_df` and `promo_df`:

#### For Loan Dataset:
- **Disparate Impact Ratio (DIR)**: Compare approval rates between groups (e.g., SC/ST vs General)
- **Equal Opportunity Difference**: Difference in true positive rates across groups
- **Accuracy by Group**

#### For Promotion Dataset:
- Treat `assigned_promotion != "No_Promo"` as the positive class (received benefit)
- Repeat similar fairness metrics (DIR, accuracy, etc.) by `caste` or `religion`

---

### ✅ Final Task

Summarize your findings:
- Do protected groups receive systematically different outcomes?
- Does removing protected features improve fairness?
- How does fairness vary between **loan approval** and **promotion exposure** tasks?

You are encouraged to structure your analysis with clear sections and interpretations.
